class Vigenère_Cipher:

    # Constructor
    def __init__(self, alphabet='abcdefghijklmnopqrstuvwxyz'):
        self.alphabet = alphabet
        self.cipher_text = ""

    # Get User Choice [Encrypt/Decrypt]
    def get_user_choice(self):
        OPTIONS = {
            '1' : 'Encrypt',
            '2' : 'Decrypt',
            '3' : 'Quit'
        }
        print("Options:")
        for index, option in OPTIONS.items():
            print(f"{index}. {option}")
        
        while True:
            try:
                choice = int(input("=> "))
                if 1 <= choice <= len(OPTIONS):
                    return choice
            except ValueError:
                print("Invalid Input!")

    # Get Message Method
    def get_message(self, crypt_choice):
        message = input(f"Type the message you want to {crypt_choice}: ")
        return message
        
    # Get Key Method
    def get_key(self):
        key = input("Type the key of the Cipher: ")
        return key
    
    # Encrypt Method
    def cipher(self, message, key, key_index, final_message, direction):
        for character in message.lower():
            if not character.isalpha():
                final_message += character
            else:
                key_character = key[key_index % len(key)]
                key_index += 1
                offset = self.alphabet.index(key_character)
                index = self.alphabet.find(character)
                new_index = (index + offset * direction) % len(self.alphabet)
                final_message += self.alphabet[new_index]
        self.cipher_text = "Encrypted" if direction == 1 else "Decrypted"
        return final_message
    
    # Run Method
    def run(self):
        final_message = ""
        key_index = 0
        while True:
            choice = self.get_user_choice()
            if choice == 3:
                break
            elif choice in (1, 2):
                crypt_choice = "Encrypt" if choice == 1 else "Decrypt"
                message = self.get_message(crypt_choice)
                key = self.get_key()
                result = self.encrypt(message, key, key_index, final_message, 1) if choice == 1 else self.encrypt(message, key, key_index, final_message, -1)
                print(f'{self.text}: ', result)


# Main method
def main():
    cipher = Vigenère_Cipher()
    cipher.run()
if __name__ == "__main__":   
    main()
