#!/usr/bin/python
'''
Ofuscate HEX :)
'''
string='this is my text to be offuscate'.encode().hex()

list_hex = [i+'@@@@' for i in string] 
print(''.join(list_hex))

# print(bytes.fromhex(st.replace('@@@@','')))