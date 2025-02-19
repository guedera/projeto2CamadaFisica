import struct

def bytes_to_float(b):
    return struct.unpack('f', b)[0]


print(bytes_to_float(b'\xc3\xf5H@'))
