'''
 # @ Author: Liqian Chen
 # @ Create Time: 2023-11-10 15:48:11
 # @ Modified by: Liqian Chen
 # @ Modified time: 2023-11-10 19:55:23
 # @ Description:
 '''


import utils
from Hill import Hill, Hill256, Hill26

def set_algorithm(plaintext, blocksize, algorithm):
    if algorithm == "hill26" or algorithm == "hill":
        return Hill26(plaintext, blocksize)
    if algorithm == "hill256":
        return Hill256(plaintext, blocksize)

def set_iv(blocksize, algorithm):
    if algorithm == "hill26" or algorithm == "hill":
        iv = utils.generate_IV(blocksize, 26)
    if algorithm == "hill256":
        iv = utils.generate_IV(blocksize, 256)
    return iv
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
        self.algorithm = set_algorithm(plaintext, blocksize, algorithm)
        print("* work mode: CBC")
        self.iv = set_iv(blocksize, algorithm)
        print("* iv: ", self.iv)
        self.algorithm.generate_key_matrix()

    def encrypt(self):
        for i in range(self.algorithm.block_cnt):

            print("--------------------BLOCK", i, "(EN)-------------------")
            self.algorithm.plain_ascii_block[i] = self.algorithm.text2ascii_block(self.algorithm.plain_text_block[i])
            print("(1)  plaintext: ", self.algorithm.plain_text_block[i], "\t==>\t", self.algorithm.plain_ascii_block[i])

            chain_input = self.iv if i == 0 else self.algorithm.cipher_ascii_block[i-1]
            print("(2)  chain input:\t\t", chain_input)
            chain_input_bin = ['' for _ in range(self.algorithm.block_size)]
            plain_ascii_bin = ['' for _ in range(self.algorithm.block_size)]
            input_bin = ['' for _ in range(self.algorithm.block_size)]
            input = []

            print("(3)  xor:")
            # handle with input of hill block encryption
            for j in range(self.algorithm.block_size):
                # cnt, chain_input_bin[j] = utils.to_bin_modulo(chain_input[j], self.algorithm.modulo)
                # _, plain_ascii_bin[j] = utils.to_bin_modulo(self.algorithm.plain_ascii_block[i][j], self.algorithm.modulo)
                # input_bin[j] = utils.xor(chain_input_bin[j], plain_ascii_bin[j], cnt)
                chain_input_bin[j] = bin(chain_input[j])
                plain_ascii_bin[j] = bin(self.algorithm.plain_ascii_block[i][j])
                input_bin[j] = (int(chain_input_bin[j], 2) ^ int(plain_ascii_bin[j], 2) )% self.algorithm.modulo
                print("",self.algorithm.plain_ascii_block[i][j],"⊕ ", chain_input[j], "==>(",plain_ascii_bin[j][2:], ") ⊕ (", chain_input_bin[j][2:], ")==>", bin(input_bin[j])[2:], "==>", input_bin[j], "( mod", self.algorithm.modulo, ")")

                input.append(input_bin[j])
            print("(4)  input:\t\t\t", input)
            self.algorithm.plain_ascii_block[i] = input
            print("(5)  encrypt:\t\t", end="\t")
            self.algorithm.cipher_ascii_block[i] = self.algorithm.encrypt_block(self.algorithm.plain_ascii_block[i])
            self.algorithm.ciphertext = self.algorithm.ciphertext + self.algorithm.ascii2text_block(self.algorithm.cipher_ascii_block[i])
        
        print("====================CIPHERTEXT===================")

        print("\t\t  ",self.algorithm.ciphertext[:0 - (self.algorithm.padding_bit)])    

            
    def decrypt(self):
        for i in range(self.algorithm.block_cnt):
            print("--------------------BLOCK", i, "(DE)-------------------")
            print("(1)  ciphertext:\t\t", self.algorithm.cipher_ascii_block[i])
            self.algorithm.decryption_block[i] = self.algorithm.decrypt_block(self.algorithm.cipher_ascii_block[i])
            chain_input = self.iv if i == 0 else self.algorithm.cipher_ascii_block[i-1]
            print("(2)  chain input:\t\t", chain_input)
            chain_input_bin = ['' for _ in range(self.algorithm.block_size)]
            decryption_bin = ['' for _ in range(self.algorithm.block_size)]
            output_bin = ['' for _ in range(self.algorithm.block_size)]
            output = []

            print("(3)  xor:")
            for j in range(self.algorithm.block_size):
                # cnt, chain_input_bin[j] = utils.to_bin_modulo(chain_input[j], self.algorithm.modulo)
                # _, decryption_ascii_bin[j] = utils.to_bin_modulo(self.algorithm.decryption_block[i][j], self.algorithm.modulo)
                # output_bin[j] = utils.xor(chain_input_bin[j], decryption_ascii_bin[j], cnt)
                # output.append(int(output_bin[j], 2) % self.algorithm.modulo)
                chain_input_bin[j] = bin(chain_input[j])
                decryption_bin[j] = bin(self.algorithm.decryption_block[i][j])
                output_bin[j] = int(chain_input_bin[j], 2) ^ int(decryption_bin[j], 2)
                print("",self.algorithm.cipher_ascii_block[i][j],"⊕ ", chain_input[j], "==>(",decryption_bin[j][2:], ") ⊕ (", chain_input_bin[j][2:], ")==>", bin(output_bin[j])[2:], "==>", output_bin[j] )

                output.append(output_bin[j])
            self.algorithm.decryption_block[i] = output
            print("(4)  decryption text:\t\t", output)

            self.algorithm.decrypt_plain = self.algorithm.decrypt_plain + self.algorithm.ascii2text_block(self.algorithm.decryption_block[i])
        print("=================DECRYPTION RESULT=================")

        print("\t\t  ", self.algorithm.decrypt_plain[:0 - (self.algorithm.padding_bit)])    



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
