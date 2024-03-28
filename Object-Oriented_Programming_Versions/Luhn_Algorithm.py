# LUHN ALGORITHM [OWN VERSION]

import os

class Luhn_Algorithm:

    # Constructor
    def __init__(self, card_number):
        self.card_number = card_number

    # Card Number Translation Method
    def card_translate(self, card_number):
        translate_card_number = str.maketrans({'-': '', ' ': ''})
        translated_card_number =  card_number.translate(translate_card_number)
        return translated_card_number
    
    # Card Number Reversal Method
    def reverse_card_number(self, translated_card_number):
        reversed_card_number = translated_card_number[::-1]
        return reversed_card_number


    # Odd Index Digit Method Calculation
    def odd_index_digits(self, reversed_card_number):
        sum_of_odd_digits = 0
        odd_digits = reversed_card_number[::2]
        for digit in odd_digits:
            try:
                sum_of_odd_digits += int(digit)
            except ValueError:
                print("INVALID CARD NUMBER. Input should only be NUMBER and/or with - or whitespaces\n")
                return main()
        return sum_of_odd_digits
            

    # Even Index Digits Method Calculation
    def even_index_digits(self, reversed_card_number):
        sum_of_even_digits = 0
        even_digits = reversed_card_number[1::2]
        for digit in even_digits:
            sum_of_even_digits += int(digit)
        return sum_of_even_digits
    
    # Total Sum Method Calculation
    def total_sum_result(self, odd_sum, even_sum):
        total = odd_sum + even_sum
        return total % 10 == 0
    
    # Check Result Method
    def check_result(self, total_sum_result):
        result = "VALID" if total_sum_result == True else "INVALID"
        return result

    # Run Method
    def run(self):
        try:
            translated_card_number = self.card_translate(self.card_number)
        except ValueError:
            print("INVALID CARD NUMBER\n")
        reversed_card_number = self.reverse_card_number(translated_card_number)
        odd_sum = self.odd_index_digits(reversed_card_number)
        even_sum = self.even_index_digits(reversed_card_number)
        total_sum_result = self.total_sum_result(odd_sum, even_sum)
        result = self.check_result(total_sum_result)
        return result

# Main Method
def main():
    while True:
        print("LUHN ALGORITHM\n")
        card_number = input("Check Your Card Number [Q to Quit]: ")
        if card_number.upper() == 'Q':
            break
        verify_card = Luhn_Algorithm(card_number)
        result = verify_card.run()
        print(f"Your Card Number is {result}.\n")
        repeat = input("AGAIN? [Y/N]: ")
        if repeat.upper() != 'Y':
            break
        os.system('cls')

if __name__ == "__main__":
    main()
