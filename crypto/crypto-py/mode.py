import utils

class EBC:
    def __init__(self, plaintext):
        self.plaintext = plaintext

    def encrypt(self):
        pass
    def decrypt(self):
        pass

class CBC:
    def __init__(self, plaintext):
        self.plaintext = plaintext
        self.iv = utils.generate_IV()
    def encrypt(self):
        pass
    def decrypt(self):
        pass

class CFB:
    def encrypt(self):
        pass
    def decrypt(self):
        pass

class OFB:
    def encrypt(self):
        pass
    def decrypt(self):
        pass
    
class CTR:
    def encrypt(self):
        pass
    def decrypt(self):
        pass
