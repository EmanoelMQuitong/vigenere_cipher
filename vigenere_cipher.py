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
