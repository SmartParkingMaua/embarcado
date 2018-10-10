import os, sys
import tensorflow as tf
from sendInfo import *
import exifread


def Classify(image_path):
        
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

	# change this as you see fit
	#image_path = sys.argv[1]
        
	#Read image Timestamp
    with open(image_path, 'rb') as fh:
        tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
        timestamp = tags["EXIF DateTimeOriginal"]

	# Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

	# Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("classifier_labels.txt")]

	# Unpersists graph from file
    with tf.gfile.FastGFile("classifier_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
	    # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	    
        predictions = sess.run(softmax_tensor, \
	             {'DecodeJpeg/contents:0': image_data})
	    
	    # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        action = label_lines[top_k[0]]
        score = predictions[0][top_k[0]]
        print("Image classified as: %s (score = %.5f)" % (action, score))

	    # Send the highest scored action 
        ValidatePost(action, score, timestamp)
