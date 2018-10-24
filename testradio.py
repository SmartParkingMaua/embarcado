from nrf24 import NRF24
import time
import RPi.GPIO as GPIO

GPIO.setup(27, GPIO.OUT) # LoRa chip enable
GPIO.setup( 5, GPIO.OUT) # Led diag

GPIO.output(27, 1) # LoRa chip enable = false

addrRx = "2Node" # ou [ 0x32, 0x4E, 0x6F, 0x64, 0x65 ]
addrTx = "1Node" # ou [ 0x31, 0x4E, 0x6F, 0x64, 0x65 ]

radio = NRF24()
radio.begin(0,0,22,24) # Pins
radio.setDataRate(NRF24.BR_250KBPS) # Max range
radio.setPALevel(NRF24.PA_MAX) # Max power
radio.openWritingPipe(addrTx) 
radio.openReadingPipe(1,addrRx)
radio.startListening()
radio.printDetails()

print ("Aguardando dados :")

try:
    while True:
        pipe = [0]
        if radio.available(pipe, False):
            GPIO.output(5 , 1) # Led diag
            print ("Recebido")
            dado = []
            radio.read(dado)
            radio.stopListening()
            radio.write(dado)
            radio.startListening()
        time.sleep(0.1)
        GPIO.output(5 , 0) # Led diag
        
except KeyboardInterrupt:
    print("Finalizado")
    GPIO.output(5 , 0) # Led diag

#sudo apt-get update
#sudo apt-get install python-dev python-rpi.gpio
#git clone https://github.com/Gadgetoid/py-spidev.git
#cd py-spidev
#sudo python setup.py install
#cd ..
#git clone https://github.com/dquadros/pynrf24.git
#cd pynrf24
#sudo python setup.py install
