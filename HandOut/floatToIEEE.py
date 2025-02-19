import struct

def float_to_ieee754(number):
    # Usa a biblioteca struct para empacotar o número em formato IEEE 754
    packed = struct.pack('>f', number)
    # Converte os bytes empacotados para uma lista de inteiros (bytes)
    byte_list = list(packed)
    return byte_list


#---------------------------------------------#

#Teste
#lista de floats
x = [1.12312, 1.23, 23.5443]

#lista que será enviada
pra_enviar = []

#converte em ieee754 e adiciona na lista pra_enviar
for i in x:
    pra_enviar += (float_to_ieee754(i))

#imprime a lista pra_enviar
print(pra_enviar)

for j in pra_enviar:
    print(hex(j))
#---------------------------------------------#