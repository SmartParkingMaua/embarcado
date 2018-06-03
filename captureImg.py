# importa bibliotecas necessarias
# Instalar o python GPIO antes da execucao: sudo apt-get install python-rpi.gpio
import SPMutils

if (__name__ == '__main__'):
    #Enche o buffer com os dados recolhidos via uart
    buff = SPMutils.readDataStream()
    buff = 'teste'
    #Realiza a execucao dos comandos recebidos, se forem validos
    SPMutils.seletorCmd(buff)
