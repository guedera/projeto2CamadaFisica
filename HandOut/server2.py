from enlace import *
import time

# Porta COM usada no Windows (ajuste se necessário)
serialName = "COM7"           

def main():
    try:
        print("Iniciando servidor de recepção (server.py)")
        com1 = enlace(serialName)
        com1.enable()
        print("Comunicação aberta.")

        print("Aguardando o recebimento de 1 byte...")
        # Recebe 1 byte
        rxBuffer, nRx = com1.getData(1)
        print("Recebeu {} byte(s): {}".format(nRx, rxBuffer))

        com1.disable()
        print("Servidor encerrado.")
        
    except Exception as erro:
        print("Ops! Ocorreu um erro:")
        print(erro)
        com1.disable()

if __name__ == "__main__":
    main()
