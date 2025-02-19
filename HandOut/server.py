#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
#####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np

#/dev/ttyACM0 ou COM7
serialName = "/dev/ttyACM0"

pra_enviar = [1.453522,45.000012,222.020301]


def main():
    try:
        print("Iniciou o main")
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()

        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)
       
        print("Abriu a comunicação")

        print("\n")
        print("Recepção iniciada!")
        print("\n")

        rxBuffer, nRx = com1.getData(1)
        print("recebeu {} bytes" .format(len(rxBuffer)))
        print("\n")

            
        # obtido = com1.rx.getNData(rxBuffer)

        print("\n")
        print("\n")

        num = int.from_bytes(rxBuffer, byteorder='big')

        print(f"OS DADOS OBTIDOS FORAM: {num}")
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        print(type(rxBuffer))
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
