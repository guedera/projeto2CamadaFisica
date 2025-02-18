# Em transmit2.py
from enlace import *
import time

serialName = "/dev/ttyACM0"  # Porta no Ubuntu

def main():
    try:
        com1 = enlace(serialName)
        com1.enable()
        if True:
            print("Comunicação aberta")
            com1.sendData(b'\x01')  # Envia um byte de teste
            print("Byte enviado")
        com1.disable()
    except Exception as erro:
        print("Erro:", erro)

if __name__ == "__main__":
    main()