#!/usr/bin/python 
# Define la clave
mensaje_cifrado = "HQERKhYCLDc9KgQX"
clave = "encryptXORkey"
mensaje_descifrado = ""

for i in range(len(mensaje_cifrado)):
    char_cifrado = mensaje_cifrado[i]
    char_clave = clave[i % len(clave)]
    char_descifrado = chr(ord(char_cifrado) ^ ord(char_clave))
    mensaje_descifrado += char_descifrado

print(mensaje_descifrado)
