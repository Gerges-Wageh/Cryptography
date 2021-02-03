import numpy as np


class HillCipher:
    def __init__(self, p, key):
        self.plainText = p
        self.encrypt(key)

    def encrypt(self, key):
        if len(key) == 4:
            cipher = open('hill_cipher_2x2.txt', 'w')
            cipherText = ''
            key = np.array(key)
            key = key.reshape(2, 2)
            for line in self.plainText:
                if line == '':
                    continue
                if len(line) % 2 == 1:
                    line += 'x'
                line = line.lower()
                cipherText += (self.keySize2x2(key, line) + '\n')
            cipher.write(cipherText)
        else:
            cipher = open('hill_cipher_3x3.txt', 'w')
            cipherText = ''
            key = np.array(key)
            key = key.reshape(3, 3)
            for line in self.plainText:
                if line == '':
                    continue
                while len(line) % 3 != 0:
                    line += 'x'
                line = line.lower()
                cipherText += (self.keySize3x3(key, line) + '\n')
            cipher.write(cipherText)

    def keySize2x2(self, key, text):
        c = ''
        for i in range(0, len(text) - 1, 2):
            p = np.array([ord(text[i]) - 97, ord(text[i + 1]) - 97])
            p = p.reshape(2, 1)
            res = np.dot(key, p) % 26
            c += (chr(res[0][0] + 97) + chr(res[1][0] + 97))
        return c

    def keySize3x3(self, key, text):
        c = ''
        for i in range(0, len(text) - 1, 3):
            p = np.array([ord(text[i]) - 97, ord(text[i + 1]) - 97, ord(text[i + 2]) - 97])
            p = p.reshape(3, 1)
            res = np.dot(key, p) % 26
            c += (chr(res[0][0] + 97) + chr(res[1][0] + 97) + chr(res[2][0] + 97))
        return c


