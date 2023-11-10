import utils
from Hill import Hill, Hill256, Hill26

def set_algorithm(plaintext, blocksize, algorithm):
    if algorithm == "hill26" or algorithm == "hill":
        return Hill26(plaintext, blocksize)
    if algorithm == "hill256":
        return Hill256(plaintext, blocksize)

def set_iv(blocksize, algorithm):
    if algorithm == "hill26" or algorithm == "hill":
        return utils.generate_IV(blocksize, 26)
    if algorithm == "hill256":
        return utils.generate_IV(blocksize, 256)
class EBC:
    def __init__(self, plaintext):
        self.plaintext = plaintext

    def encrypt(self):
        pass
    def decrypt(self):
        pass

class CBC:
    def __init__(self, plaintext, blocksize, algorithm):
        self.plaintext = plaintext
        self.iv = set_iv(blocksize, algorithm)
        self.algorithm = set_algorithm(plaintext, blocksize, algorithm)

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
