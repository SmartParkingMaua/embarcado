# importa bibliotecas necessarias
# Instalar o python GPIO antes da execucao: sudo apt-get install python-rpi.gpio
from SPMutils import *
from nrf24 import NRF24
import time
import RPi.GPIO as GPIO

def CaptureImg():
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
    camInit()       #camera initialization

    print ("Aguardando dados :")

    try:
        while True:
            pipe = [0]
            if radio.available(pipe, False):
                GPIO.output(5 , 1) # Led diag
                print ("Recebido")
                captureImg()        #take picture if trigger received
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

if (__name__ == '__main__'):
    CaptureImg()
