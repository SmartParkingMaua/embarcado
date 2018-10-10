# SmartParking Mauá


## Installation Guide


### Installing Raspbian 8.0 "Jessie"
Navigate to: ``http://downloads.raspberrypi.org/raspbian/images/``

Click on ``Raspbian-2017-03-03`` folder.

Download the OS image (I recommend zip file).

Extract the zip file.

Use **Etcher** or **Rufus** to create the bootable SD card (I recommend to fully format the pen drive before doing that).

After the bootable SD card has been created, plug it in the Raspberry Pi and start the device. Open the terminal and execute the following command:
```
sudo apt-get update && sudo apt-get dist-upgrade -y
```

I also recommend to install vim as text editor:
```
sudo apt-get install vim
```


### Installing TensorFlow
In order to install TensorFlow, run the following commands:
```
sudo apt install libatlas-base-dev
pip3 install tensorflow
```
For further information, visit: ``https://github.com/samjabrahams/tensorflow-on-raspberry-pi``


### Installing GPIO
Use the following command to install GPIO dependencies:
```
sudo apt-get install python-rpi.gpio
```
## Installing EXIFread
```
$ pip3 install exifread
```

### Cloning SD card image
In case you want to clone SD card after everything has been installed, you can use the ``imageUSB`` program at: ``https://imageusb.br.uptodown.com/windows``

If you have any doubts on how to use it, take a look on the following tutorial: ``https://www.tecmundo.com.br/pendrive/54921-criar-imagem-pendrive-clona-lo.htm``


### Cloning git repository
Download the solution using the following command (It is recommended to clone it into *HOME* folder):
```
git clone "https://github.com/SmartParkingMaua/embarcado.git"
```

### Running the solution
In order to run the solution, you will need a webcam supported by the ``pygame library`` and a proximity sensor connected in the IOs shown in the image below:

![Sensor setup](sensor_setup.jpg?raw=true "Sensor setup")

Feel free to change the code in order to make it runnable with your ends.

Having everything set up, go to ``embarcado`` folder and execute the following commands in different terminals:

```
python3 captureImg.py
python3 classifyImg.py
```

The former is responsable for capturing the images when the sensor detects something within its range.
The later is responsable for classifying and deleting the images and posting the results into the database.

If you want to see the images being captured and deleted, check the ``SmartParkingMaua/images`` folder inside ``HOME`` folder.

And that's it!

In case you have any problems, improvements or tips, please let us know.
