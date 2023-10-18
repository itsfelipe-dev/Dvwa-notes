#!/usr/bin/python 

import math
import os 




def file_entropy(filename):
    with open(filename, 'rb') as file:
        data = file.read()

    # Create a dictionary to count the occurrences of each byte in the file
    byte_counts = {}
    total_bytes = len(data)

    for byte in data:
        if byte in byte_counts:
            byte_counts[byte] += 1
        else:
            byte_counts[byte] = 1

    # Calculate entropy
    entropy = 0.0
    for count in byte_counts.values():
        probability = count / total_bytes
        entropy -= probability * math.log2(probability)

    return entropy
for filename in os.listdir('./'):
	if not filename == 'source':
		entropy = file_entropy(filename)
		print(f'Entropy for {filename}:, {round(entropy,2)} bits per byte')
