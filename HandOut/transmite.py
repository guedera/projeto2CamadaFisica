#!/usr/bin/env python3
from enlace import enlace
import time

def main():
    # Substitua 'COMx' pela porta serial correta do seu Arduino1
    serialName = "/dev/ttyACM0"
    print("Transmissor inicializado na porta {}".format(serialName))
    
    # Instancia a camada de enlace e habilita a comunicação
    com = enlace(serialName)
    com.enable()
    time.sleep(2)

    # Cria buffer com 1 byte: "\x13"
    txBuffer = b"\x13"
    print("Transmitindo o byte: {}".format(txBuffer))
    
    # Envia o dado
    com.sendData(txBuffer)

    # Aguarda até que a transmissão seja concluída
    while com.tx.getIsBussy():
        time.sleep(0.1)
    print("Transmissão finalizada!")

    # Desabilita a comunicação
    com.disable()

if __name__ == '__main__':
    main()
