from Hill import Hill, Hill256, Hill26
import utils
import numpy as np
from mode import CBC

# cbc = CBC("fdsziocdizo", 5, "hill")

test = Hill26("fdsziocdizo", 5)
test.encrypt()
test.decrypt()

test = Hill256("fdsziocdizo", 5)
test.encrypt()
bin_cipher = 0
for i in range(len(test.decryption_block)):
    for j in range(len(test.cipher_block[0])):
        print(test.cipher_block[i][j], ": ", bin(test.cipher_block[i][j]))

test.decrypt()