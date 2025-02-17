from enlace import *
import time
import numpy as np

serialName = "COM7"  # Porta no Windows

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        
        com1.enable()
        print("Abriu a comunicação")

        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        if nRx > 0:
            print("Recebeu o byte de sacrificio:", rxBuffer)
        else:
            print("Não recebeu o byte de sacrificio")
        com1.rx.clearBuffer()
        time.sleep(.1)
        
        print("\n")
        print("Recepção iniciada!")
        print("\n")

        while com1.rx.getIsEmpty():  
            time.sleep(.05)
        
        while com1.tx.getIsBussy():
            time.sleep(.05)

        txlen = com1.tx.getBufferLen()
        rxBuffer, nRx = com1.getData(txlen)
        print("recebeu {} bytes" .format(len(rxBuffer)))
        print("\n")

        obtido = com1.rx.getNData(rxBuffer)

        print("\n")
        print("\n")

        print(f"OS DADOS OBTIDOS FORAM: {obtido}")
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