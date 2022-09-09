class CeaserCipher:
    def __init__(self) -> None:
        pass

    def encrypt(self, text, key):
        return text

    def decrypt(self,text):
        return text
    
    def process_request(self, text, option, key=None):
        print(text, option,key)
        option = int(option)
        if (option == 1 and key != None):
            return self.encrypt(text, key)
        elif (option == 2):
            return self.decrypt(text)