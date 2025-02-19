import struct

def float_to_ieee754(numbers):
    ieee_list = []
    for number in numbers:
        # Usa a biblioteca struct para empacotar o número em formato IEEE 754
        packed = struct.pack('>f', number)
        # Converte os bytes empacotados para uma lista de inteiros (bytes)
        byte_list = list(packed)
        # Converte cada byte para hexadecimal e adiciona à lista
        ieee_list.extend([hex(byte) for byte in byte_list])
    return ieee_list

# Exemplo de uso
x = [1.12312, 1.23, 23.5443]
ieee754_list = float_to_ieee754(x)

# Imprime a lista de bytes em hexadecimal
print(ieee754_list)