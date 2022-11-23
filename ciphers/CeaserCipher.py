class CeaserCipher:
    def __init__(self) -> None:
        pass

    def encrypt(self, text, key):  
        text =text.replace(" ","")
        result=""  #empty string
        for i in range(len(text)):
            char=text[i]
            if(char.isupper()):  #if the text[i] is in upper case
                result=result+chr((ord(char)+key-65)%26+65)
            else:
                result=result+chr((ord(char)+key-97)%26+97)
        return result

    def decrypt(self,text, key):
        # Cipher(n) = De-cipher(26-n)
        key = 26-key 
        
        result=""  #empty string
        for i in range(len(text)):
            char=text[i]
            if(char.isupper()):  #if the text[i] is in upper case
                result=result+chr((ord(char)+key-65)%26+65)
            else:
                result=result+chr((ord(char)+key-97)%26+97)
        return result
    
    def process_request(self, text, option, key=None):
        print(text, option,key)
        option = int(option)
        key = int(key)
        if (option == 1 and key != None):
            return self.encrypt(text, key)
        elif (option == 2):
            return self.decrypt(text, key)