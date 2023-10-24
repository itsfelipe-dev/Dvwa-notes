#!/usr/bin/python 
from itertools import izip, cycle

mensaje_cifrado = "XORprocedure"
clave = "awesomepassword"

xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(mensaje_cifrado, cycle(clave)))

print(xored)



# mensaje_descifrado = ""
# for i in range(len(mensaje_cifrado)):
#     char_cifrado = mensaje_cifrado[i]
#     char_clave = clave[i % len(clave)]
#     char_descifrado = chr(ord(char_cifrado) ^ ord(char_clave))
#     mensaje_descifrado += char_descifrado

# print(mensaje_descifrado)

