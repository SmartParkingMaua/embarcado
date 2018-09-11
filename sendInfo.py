# Import libraries
import requests
import time
import configparser
import json
import SPMutils


# Set minimum precision for post validation
minPrecision = 0.7


def ValidatePost(action, score, timestamp):
    # Check if the current action is different than "others" classification
    if ((action == "entrance") or (action == "exit")):
        # Check if the current score is higher than the minimum acceptable precision
        if (score > minPrecision):
            Post(action, timestamp)
        else:
            print("Image score is lower than the minimum precision (%.2f)" % minPrecision)


def Post(action, timestamp):
    # Initialize INI file
    config = configparser.ConfigParser()
    config.read('localInfo.ini')
    
    # Set JSON variables
    gate = idRaspb()

    # Send information
    url = 'https://smartparkingmaua.000webhostapp.com/'
    x = {
        "idEstacionamento": gate,
        "timestamp": timestamp,
        "estado": action
    }
    
    payload = json.dumps(x)

    # Set post URL
    r = requests.post(url, json=payload)
    print("Post status: %i" % r.status_code)
