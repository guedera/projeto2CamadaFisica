from enlace import *
import time
import numpy as np

serialName = "COM7"

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        
        com1.enable()


        print("comecando BS")
        time.sleep(2)
        com1.sendData(b'00')
        time.sleep(1)
        print("enviando bit de sacrificio")
        
        print("Abriu a comunicação")
        txBuffer = b'\x13' 
        
        print("Meu array de bytes tem tamanho {}" .format(len(txBuffer)))
        
        print("Transmissão iniciada!")
        com1.sendData(np.asarray(txBuffer))
        time.sleep(2)
        
        txSize = com1.tx.getStatus()
        print('enviou = {} bytes' .format(txSize))
        
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
