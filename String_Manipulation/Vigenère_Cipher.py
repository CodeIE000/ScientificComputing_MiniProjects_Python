# VIGENERE CIPHER [TUTORIAL CODE]

# text = 'mrttaqrhknsw ih puggrur'
text = 'freecodecamp is awesome'
custom_key = 'happycoding'

# Cipher Algorithm
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            print(key_char, "= key_char")
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            print(offset, "= offset")
            index = alphabet.find(char)
            print(char, "= char")
            print(index, " = index")
            new_index = (index + offset*direction) % len(alphabet)
            print(new_index, " = new_index")
            final_message += alphabet[new_index]
            print("reset loop\n")
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, 1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')