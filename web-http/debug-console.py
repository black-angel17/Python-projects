binary_string = "0011011001100100001100000011100101100110001101100011010000110001001110000110001000110100011000110011001100110010001100110011010000110110001100110011001001100001011000110011001100110110001100110110010101100110001100100011100100110001011000100110011001100110001011100110111001101001011011100110101001100001"

# Convert binary string to bytes
byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))


print(byte_array)
# Convert bytes to string
decoded_text = byte_array.decode('utf-8')

print(decoded_text)
