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
