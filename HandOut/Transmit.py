from enlace import *
import time
import numpy as np

serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        
        com1.enable()
        print("Abriu a comunicação")

        time.sleep(.2) 
        com1.sendData(b'00') 
        time.sleep(1)

        print('\n')
        print("Enviou o bit de sacrifício.")
        
        txBuffer = b'\x13\x12'
        
        print("Meu array de bytes tem tamanho {}" .format(len(txBuffer)))
        
        print("Transmissão iniciada!")
        com1.sendData(np.asarray(txBuffer))  #as array apenas como boa pratica para casos de ter uma outra forma de dados
        
        txSize = com1.tx.getStatus()
        print('enviou = {} bytes' .format(txSize))
        
        txLen = len(txBuffer)

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
