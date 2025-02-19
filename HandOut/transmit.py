from enlace import *
import time
import numpy as np
from floatToIEEE import float_to_ieee754
from IEEEToFloat import ieee754_to_float
import os

serialName = "/dev/ttyACM0"

lista = [1.3424, 54.45544, 200.002]
soma_lista = sum(lista)

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        com1.enable()
        os.system('clear')

        print("Enviando o byte de sacrifício")
        com1.sendData(b'00')
        print("Byte de sacrifício enviado!\n")
        time.sleep(2)
        os.system('clear')

        print("Vou mandar quantos números serão enviados!")
        txBuffer = bytearray([len(lista)])
        print("Estou enviando {} números flutuantes!\n" .format(len(lista)))
        com1.sendData(np.asarray(txBuffer))
        print("Enviado!")
        time.sleep(2)
        os.system('clear')

        print("Abriu a comunicação! Vou enviar a lista de Floats!\n")
        # Converte a lista de floats para o formato IEEE 754
        txBuffer = bytearray(float_to_ieee754(lista))
        
        print("Meu array de bytes tem tamanho {}\n" .format(len(txBuffer)))
        
        com1.sendData(np.asarray(txBuffer))
        print("Enviado!")
        time.sleep(2)
        os.system('clear')

        txSize = com1.tx.getStatus()
        print('enviou = {} bytes!' .format(txSize))
        time.sleep(2)
        os.system('clear')

        print("Esperando a soma!")
        rxBuffer, nRx = com1.getData(1)
        os.system('clear')

        print("Recebeu a soma!")
        retorno = ieee754_to_float(rxBuffer)
        print("O resultado da soma é: ", retorno)
        time.sleep(2)

        if soma_lista == retorno:
            print("Soma correta!")
        else:
            print("Soma errada!")
        time.sleep(2)

        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        
if __name__ == "__main__":
    main()