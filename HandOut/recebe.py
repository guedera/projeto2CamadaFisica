#!/usr/bin/env python3
from enlace import enlace
import time

def main():
    # Substitua 'COMx' pela porta serial correta do seu Arduino2
    serialName = "/dev/ttyACM0"
    print("Receptor inicializado na porta {}".format(serialName))
    
    # Instancia a camada de enlace e habilita a comunicação
    com = enlace(serialName)
    com.enable()
    time.sleep(2)

    print("Aguardando recebimento de dados...")
    # Aguarda e lê 1 byte recebido
    rxBuffer, nRx = com.getData(1)
    
    print("Recebido {} byte(s): {}".format(nRx, rxBuffer))

    # Desabilita a comunicação
    com.disable()

if __name__ == '__main__':
    main()
