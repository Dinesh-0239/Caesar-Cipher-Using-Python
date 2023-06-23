"""
Date: 23/06/2023 
Created by: Dinesh Singh
This is Basic Python Project based on implementing "Caesar Cipher" used to encrypt and decrypt input text according to the no. of shift.

"""
from alphabets_symbols_numbers_logo import alphabet, symbol, number, logo

def caesar_cipher(entered_text,shift_amount,direction_given):
    output_text = ""
    for letter in entered_text:
        if letter in alphabet:
            character = alphabet
            round_factor = len(alphabet)
        elif letter in symbol:
            character = symbol
            round_factor = len(symbol)
        else:
            character = number
            round_factor = len(number)
        position = character.index(letter)
        if direction_given == "encode":
            new_postion = position + shift_amount
            output_text += character[new_postion % round_factor]
        else:
            new_postion = position - shift_amount
            while new_postion < - round_factor:
                new_postion += round_factor
            output_text += character[new_postion] 
    print(f"The {direction_given}d text is {output_text}")  

choice = True
while choice:
    print("-"*80)
    print(logo)
    print("-"*80)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode","decode"]:
        print("Invalid Choice!")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(entered_text=text,shift_amount=shift,direction_given=direction)
    if input("Do you want to 'encode' or 'decode' more text?[Y:n]\n").upper() != 'Y':
        choice = False
