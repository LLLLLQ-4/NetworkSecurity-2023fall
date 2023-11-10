import numpy as np
import utils
class Hill:
    def __init__(self, plaintext, blocksize, modulo):
        self.block_size = blocksize
        self.modulo = modulo
        self.padding_bit = self.block_size - ( len(plaintext)  % self.block_size )     
        self.block_cnt = int(len(plaintext) / self.block_size) if self.padding_bit == 0 else int( (len(plaintext) + self.padding_bit) / self.block_size)

        self.plaintext = plaintext+ ''.join(plaintext[-1:] for i in range(self.padding_bit))
        self.plain_block = [self.plaintext[i * self.block_size :(i+1) * self.block_size] for i in range(self.block_cnt)]

        self.key_matrix = []
        self.key_matrix_iv = []
        self.key_matrix_generated = False        
        
        self.cipher_block = ['' for i in range(self.block_cnt)]
        self.ciphertext = ''

        self.decryption_block = ['' for i in range(self.block_cnt)]
        self.decrypt_plain = ''

    # generate key matrix, specifically, key matrix is able to inverse, and calculate inverse key matrix
    def generate_key_matrix(self):
        key_matrix = np.random.randint(0, self.modulo, [self.block_size, self.block_size])
        det = round(np.linalg.det(key_matrix)) % self.modulo
        det_inverse = utils.modulo_inverse(det, self.modulo)
        while det == 0 or det_inverse == "non inverse":
            key_matrix = np.random.randint(0, self.modulo, [self.block_size, self.block_size])
            det = round(np.linalg.det(key_matrix)) % self.modulo
            det_inverse = utils.modulo_inverse(det, self.modulo)
        self.key_matrix = key_matrix
        print("key_matrix:\n",self.key_matrix)
        # TODO: inverse of the key matrix
        self.key_matrix_iv = utils.modulo_matrix_inverse(self.key_matrix, self.modulo)
        print("key_matrix_iv:\n", self.key_matrix_iv)
        self.key_matrix_generated = True

    def ascii2text_block(self, ascii_block):
        pass

    def text2ascii_block(self, text_block):
        pass
    
    # implement the encryption of one block
    def encrypt_block(self, text_block):
        if not self.key_matrix_generated:
            self.generate_key_matrix()
        ascii_block = self.text2ascii_block(text_block)

        cipher_block = np.dot(ascii_block, self.key_matrix)

        for i in range(len(cipher_block)):
            cipher_block[i] = cipher_block[i] % self.modulo
        
        ciphertext_block = self.ascii2text_block(cipher_block)
        
        return ciphertext_block

    # implement the decryption of one block
    def decrypt_block(self, cipher_block):
        ascii_block = self.text2ascii_block(cipher_block)

        plain_block = np.dot(ascii_block, self.key_matrix_iv)

        for i in range(len(plain_block)):
            plain_block[i] = plain_block[i] % self.modulo
        plaintext_block = self.ascii2text_block(plain_block)

        return plaintext_block

    def encrypt(self):
        for i in range(self.block_cnt):
            self.cipher_block[i] = self.encrypt_block(self.plain_block[i])
            self.ciphertext = self.ciphertext + str(self.cipher_block[i])
        print(self.ciphertext[:0 - (self.padding_bit)])    

    def decrypt(self):
        for i in range(self.block_cnt):
            self.decryption_block[i] = self.decrypt_block(self.cipher_block[i])
            self.decrypt_plain = self.decrypt_plain + str(self.decryption_block[i])
        print(self.decrypt_plain[:0 - (self.padding_bit)])    

# hill with modulo 26: only for lowercase letters
class Hill26(Hill):

    def __init__(self, plaintext, blocksize):
        super().__init__(plaintext, blocksize, 26)

    # turn text into ascii order (mod 26)
    def text2ascii_block(self, text_block):
        ascii_block = np.arange(self.block_size)

        for i in range(self.block_size):
            ascii_block[i] = ord(text_block[i]) - ord('a')

        return ascii_block
    
    # turn the ascii order (mod 26) into text
    def ascii2text_block(self, ascii_block):
        text_block = ''

        for i in range(self.block_size):
            text_block = text_block + chr(ascii_block[i] + ord('a'))
        
        return text_block

# hill with modulo 256: for ascii
class Hill256(Hill):
    def __init__(self, plaintext, blocksize):
        super().__init__(plaintext, blocksize, 256)

    # turn text into ascii 
    def text2ascii_block(self, text_block):
        ascii_block = np.arange(self.block_size)

        for i in range(self.block_size):
            ascii_block[i] = ord(text_block[i])

        return ascii_block
    
    # turn the ascii into text
    def ascii2text_block(self, ascii_block):
        text_block = ''

        for i in range(self.block_size):
            text_block = text_block + chr(ascii_block[i])
        
        return text_block
