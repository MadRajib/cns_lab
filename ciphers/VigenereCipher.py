import string
lower = string.ascii_lowercase


class VigenereCipher:
    def __init__(self) -> None:
        pass

    def encrypt(self, text, key):
        index=0
        cipher_text=""

        # convert into lower case
        plain_text=text.lower()
        key=key.lower()
        
        # For generating key, the given keyword is repeated
        # in a circular manner until it matches the length of 
        # the plain text.
        for c in plain_text:
            if c in lower:
                # to get the number corresponding to the alphabet
                off=ord(key[index])-ord('a')
                
                # implementing algo logic here
                encrypt_num=(ord(c)-ord('a')+off)%26
                encrypt=chr(encrypt_num+ord('a'))
                
                # adding into cipher text to get the encrypted message
                cipher_text+=encrypt
                
                # for cyclic rotation in generating key from keyword
                index=(index+1)%len(key)
            # to not to change spaces or any other special
            # characters in their positions
            else:
                cipher_text+=c

        return cipher_text

    def decrypt(self,text, key):
        index=0
        decrypt_text=""

        # convert into lower case
        cipher_text=text.lower()
        key=key.lower()
        
        for c in cipher_text:
            if c in lower:
                # to get the number corresponding to the alphabet
                off=ord(key[index])-ord('a')

                positive_off=26-off
                decrypt=chr((ord(c)-ord('a')+positive_off)%26+ord('a'))
                
                # adding into plain text to get the decrypted messag
                decrypt_text+=decrypt
                
                # for cyclic rotation in generating key from keyword
                index=(index+1)%len(key)
            else:
                decrypt_text+=c

        return decrypt_text
    
    def process_request(self, text, option, key=None):
        print(text, option,key)
        option = int(option)
        if (option == 1 and key != None):
            return self.encrypt(text, key)
        elif (option == 2):
            return self.decrypt(text, key)

if (__name__ == "__main__") :
    crypto = VigenereCipher()
    text = crypto.encrypt("This is the plain text", "awesome world")
    print(text)
    text = crypto.decrypt(text,"awesome world")
    print(text)