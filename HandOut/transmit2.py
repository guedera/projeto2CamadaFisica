from enlace import *
import time
import numpy as np

# Porta usada no Ubuntu (ajuste se necessário)
serialName = "/dev/ttyACM0"           

def main():
    try:
        print("Iniciando transmissão (Transmite.py)")
        com1 = enlace(serialName)
        com1.enable()
        print("Comunicação aberta.")

        # Prepara 1 byte para enviar (por exemplo, 0xAA)
        txBuffer = np.asarray([0xAA], dtype=np.uint8)
        print("Enviando 1 byte...")
        com1.sendData(txBuffer)

        # Verifica quantos bytes foram efetivamente enviados
        txSize = com1.tx.getStatus()
        print("Enviados {} byte(s).".format(txSize))

        com1.disable()
        print("Transmissão encerrada.")
        
    except Exception as erro:
        print("Ops! Ocorreu um erro:")
        print(erro)
        com1.disable()

if __name__ == "__main__":
    main()
