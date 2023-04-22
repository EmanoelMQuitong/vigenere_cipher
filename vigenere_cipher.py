#vigenere cipher created
import pyfiglet
from colored import fg

#Definition of plain_casing is defined. It replaces all letter charaters to uppercase. It also removes spaces from input messages.
def plain_case(plain_text):
    plain_text = plain_text.upper()
    plain_text = plain_text.replace(" ","")
    return plain_text

#Definition of key_casing is defined. It replaces all letter charaters to uppercase. It also removes spaces from input key messages.
def key_case(key_text):
    key_text = key_text.upper()
    key_text = key_text.replace(" ","")
    return key_text

#Iteration function is created. It enables the user to repeatedly process each letter of the message and the key message.
def iteration(plain_text, key_text  ):
    iter_key = ''
    i = 0
    result_plain = plain_case(plain_text)
    result_key = key_case(key_text)
    for char in result_plain:
        if char.isalpha():
            iter_key += result_key[i % len(result_key)]
            i += 1
        else:
            iter_key += ''
    return iter_key

#encrypt_char_sol function is defined. It allows the user to process each character from iteration function. These characters are changed into ascii code, plain_char_iterate is added to its respective key_char_iterate. If it is greater than 26, modulus is applied. 
def encrypt_char_sol(plain_char, key_char, mod_list = 'encrypt'):
    if plain_char.isalpha():
        first_letter = 'a'
        if plain_char.upper():
            first_letter = 'A'
        
        plain_char_iterate = ord(plain_char) - ord(first_letter)
        key_char_iterate = ord(key_char) - ord(first_letter)


        if mod_list == 'encrypt':
            new_char_pos = (plain_char_iterate + key_char_iterate) % 26
        else:
            new_char_pos = (plain_char_iterate - key_char_iterate + 26) % 26
        return chr(new_char_pos + ord(first_letter))
    return plain_char

#encrypt_char function is defined. This function prints the ciphered text from plain characters to its corresponding key characters
def encrypted_char(plain_text, key_text):
    ciphertext = ''
    plain_text = plain_case(plain_text)
    iter_key = iteration(plain_text, key_text) 
    for plaintext_char, key_char in zip(plain_text, iter_key):
        ciphertext += encrypt_char_sol(plaintext_char, key_char) + ' '
    return ciphertext