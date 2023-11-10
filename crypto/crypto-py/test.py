
from Hill import Hill, Hill256, Hill26
import utils
import numpy as np
from mode import CBC

cbc = CBC("fdsz", 2, "hill")
# a = bin(123)
# print(a)
# b = bin(12)
# print(b)
# print(bin(int(a,2) ^ int(b,2)))
print("=====================ENCRYPTION===================")
cbc.encrypt()
print("\n\n\n\n=====================DECRYPTION===================")

cbc.decrypt()

# print(bin(1 << 5))

# test = Hill26("fdsziocdizo", 5)
# test.encrypt()
# test.decrypt()

# test = Hill256("fdsziocdizo", 5)
# test.encrypt()
# bin_cipher = 0
# for i in range(len(test.decryption_block)):
#     for j in range(len(test.cipher_block[0])):
#         # print(test.cipher_block[i][j], ": ", bin(test.cipher_block[i][j]))


# test.decrypt()