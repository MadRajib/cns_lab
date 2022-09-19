# Multiplicative cipher
from curses.ascii import isalpha
from re import T
import string
lower = string.ascii_lowercase

def keyinverse(a, m) :
    for i in range(1, m) :
        if (((a % m) * (i % m)) % m == 1) :
            return i
    return -1 ;

class AffineCipher:
    def __init__(self) -> None:
        pass

    def encrypt(self, text, key = [1,1]):
        cipher_text = ""
        for c in text:
            if not c.isalpha():
                cipher_text += c
                continue
            
            _ord = lower.index(c)

            c_ord = (_ord * key[0] + key[1]) % 26
            t = lower[c_ord]
            cipher_text += t

        return cipher_text

    def decrypt(self,text, key = [1,1]):
        decrypt_text = ""
        for c in text:
            if not c.isalpha():
                decrypt_text+=c
                continue

            _ord = lower.index(c)

            c_ord = ((_ord - key[1]) * keyinverse(key[0], 26)) % 26
            t = lower[c_ord]

            decrypt_text+= t

        return decrypt_text
    
    def process_request(self, text, option, key=None):
        print(text, option,key)
        option = int(option)
        if (option == 1 and key != None):
            return self.encrypt(text, key)
        elif (option == 2):
            return self.decrypt(text)

if (__name__ == "__main__") :
    crypto = AffineCipher()
    text = crypto.encrypt("hello world!",[3,5])
    print(text)
    text = crypto.decrypt(text,[3,5])
    print(text)