from enlace import *
import time
from IEEEToFloat import bytes_to_float

serialName = "/dev/ttyACM0"

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        
        com1.enable()
        time.sleep(2.0)
        

        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(2)
       
        print("Abriu a comunicação")

        print("\n")
        print("Recepção iniciada!")
        print("\n")

        rxBuffer, nRx = com1.getData(12)
        print("recebeu {} bytes".format(nRx))
        print("\n")

        if nRx == 12:
            floats = [bytes_to_float(rxBuffer[i:i+4]) for i in range(0, 12, 4)]
            for float in floats:
                print("Valores floats recebidos:", {float} )
        else:
            print("Número de bytes recebido é inadequado.")

        print("\n")
        print("\n")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()

if __name__ == "__main__":
    main()
