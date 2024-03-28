# CAESAR CIPHER
class CaesarCipher:
  """
  This class implements the Caesar Cipher algorithm for encryption and decryption.
  """
  def __init__(self, alphabet='abcdefghijklmnopqrstuvwxyz'):
    """
    Initializes the CaesarCipher object with an alphabet (default lowercase).
    """
    self.alphabet = alphabet

  def get_shift(self):
    """
    Prompts the user for a valid shift value and returns it.
    """
    while True:
      try:
        shift = int(input("Enter a shift value (positive for encryption, negative for decryption): "))
        return shift % len(self.alphabet)  # Ensure offset stays within alphabet range
      except ValueError:
        print("Invalid input. Please enter an integer.")

  def get_message(self):
    """
    Prompts the user for a message and returns it.
    """
    message = input("Enter your message: ")
    return message

  def encrypt(self):
    """
    Encrypts a message using the Caesar Cipher algorithm.
    """
    encrypted_text = ''
    for char in self.message.lower():
      if char.isalpha():
        index = self.alphabet.find(char)
        new_index = (index + self.offset) % len(self.alphabet)
        encrypted_text += self.alphabet[new_index]
      else:
        encrypted_text += char  # Preserve spaces and other characters
    return encrypted_text

  def decrypt(self):
    """
    Decrypts a ciphertext using the Caesar Cipher algorithm.
    """
    decrypted_text = ''
    for char in self.message.lower():
      if char.isalpha():
        index = self.alphabet.find(char)
        new_index = (index - self.offset) % len(self.alphabet)
        decrypted_text += self.alphabet[new_index]
      else:
        decrypted_text += char  # Preserve spaces and other characters
    return decrypted_text

  def run(self):
    """
    Prompts the user for options (encrypt or decrypt) and performs the operation.
    """
    while True:
      choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
      if choice == 'q':
        break
      elif choice in ('e', 'd'):
        self.offset = self.get_shift()
        self.message = self.get_message()
        if choice == 'e':
          result = self.encrypt()
          print("Encrypted Text:", result)
        else:
          result = self.decrypt()
          print("Decrypted Text:", result)
      else:
        print("Invalid choice. Please enter 'e', 'd', or 'q'.")

def main():
 """
 Starts the Caesar Cipher program and allows for repeated use.
 """
 cipher = CaesarCipher()
 while True:
   cipher.run()
   choice = input("Do you want to perform another operation? (y/n): ").lower()
   if choice != 'y':
     break

if __name__ == "__main__":
  main()































# text = 'Hello Zaira'
# shift = 3

# # Cipher Algorithm
# def caesar(message, offset):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     encrypted_text = ''

#     for char in message.lower():
#         if char == ' ':
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print('plain text:', message)
#     print('encrypted text:', encrypted_text)

# caesar(text, shift)