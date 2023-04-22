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

#input for message and key for vigenere cipher
plain_text = input("Kindly enter the message:")
key_text = input("Kindly enter the key this time:")

#declare cipher text from funciton encrypted_char
ciphertext = encrypted_char(plain_text, key_text)

#print result as ciphertext
print('\n', f"CIPHERTEXT: ",'\n', ciphertext)

#Unable to use the previous definition functions to list add values of key and text messages.
#Create alternative way
#Preparation for
print(f"LIST OF SUMS OF ENCRYPTED MESSAGE AND KEY:")

#Chars  is declared for each letter from input is converted to ascii code.
Cchars = {chr(i):i-ord('A') for i in range(ord('A'), ord('A')+26)}

#result_plain converts entered text to upper case and removes spaces. plain_text_numbers lists each ascii code per character from the message."
result_plain = plain_case(plain_text)
plain_text_numbers = (Cchars[i] for i in result_plain)

#Creat the same function for key text. However, the length of plain_text should be equal to the length of key_text
Result_key = key_case(key_text)
if len(result_plain) == len(Result_key):
    Rchars = {chr(i):i-ord('A') for i in range(ord('A'), ord('A')+26)}
    key_text_numbers = (Rchars[i] for i in Result_key)
#If the length of key case is not equal to the length of plain_case, key_case characters is repeated with its respective sequence until it is equal to the length of the message
else:
    key_code = ''
    i = 0
    for chars in result_plain:
        key_code += Result_key[i % len(Result_key)]
        i += 1
    else:
        key_code += ''
    Rchars = {chr(i):i-ord('A') for i in range(ord('A'), ord('A')+26)}
    key_text_numbers = (Rchars[i] for i in Result_key)