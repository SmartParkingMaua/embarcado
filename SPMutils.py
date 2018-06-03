# importa bibliotecas necessarias
# Instalar o python GPIO antes da execucao: sudo apt-get install python-rpi.gpio
# Instalar serial antes da execucao com: sudo apt-get install python-serial
# Liberar porta serial com: sudo raspi-config
import time
import RPi.GPIO as GPIO
import sys
import pygame.camera
import pygame.image
import serial

# inicializa camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (176,144))
cam.start()

#Funcao que define o id do aparelho relacionado ao switch selector
def idRaspb():
    #Configura modo de entrada de pinos
    GPIO.setmode(GPIO.BOARD)
    #Pinos de entrada DIP Switch
    pins = [3,5,7,8,10,11,12]
    
    #Seta Pinos como entrada c/ pull-up
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #Aguarda
    time.sleep(0.01)
    #Contador
    i = 1
    #Cria a string que será o id do aparelho
    output = ''
    
    #Monta a string (invertida)
    for pin in pins:
        if not GPIO.input(pin):
            output += '1' 
        else:
            output += '0' 
        i += 1
        
    #inverte a string para ficar correta
    output = output[::-1]
    #Converte de string binaria pra int(pode mudar depdendo do resto das funcoes)
    output = int(output, 2)
    #retorna o id do aparelho em int
    return output

#Funcao que le o datastream do rf
def readDataStream():
    ser = serial.Serial ("/dev/ttyAMA0")    #Abre a porta de nome xxx, Usando GPIO 14 e 15 como Rx/Tx 
    ser.baudrate = 9600                     #Setar baud rate para 9600
    dataBuff = ser.read(10)                     #Le 10 digitos do serial
    ser.close()
    #Talvez algumas manipulacoes sejam necessarias...
    #.
    #.
    data = databuff
    return data

#definicao do seletor de comandos
def seletorCmd(cmd):
    #Verifica se o aparelho é o alvo da transmissao
    if(cmd[0] == idRaspb()):
        #Switch case para executar o comando recebido
        switcher = {
            0: "teste",
            1: captureImg,
        }
        return switcher.get(cmd, "nothing")

#Funcao utilizada para capturar as imagens
def captureImg():
    # inicializa/retorna o contador pra 1, uma vez que as imagens sao deletas conforme são classificadas
    imgCount=1

    # define nome da imagem
    imgName = "img_" + str(imgCount) + ".jpg"

    # procura pelo nome de imagem disponivel mais proximo
    while(Find(imgName, imgPath) != None):
        imgCount+=1
        imgName = "img_" + str(imgCount) + ".jpg"
    
    #captura a imagem, e necessario rodar 3x por motivos tecnicos do momento
    img = cam.get_image()
    img = cam.get_image()
    img = cam.get_image()

    # define o nome da imagem de acordo com o numero do contador e a salva localmente
    imgFullPath = imgPath + '/' + imgName
    pygame.image.save(img, imgFullPath)
    
    #imprime o nome da imagem gerada para o log
    print("Saved image name: " + imgName)
