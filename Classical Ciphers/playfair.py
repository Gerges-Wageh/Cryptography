from collections import OrderedDict
from itertools import product


class PlayFairCipher:
    def __init__(self, p, key):
        self.plainText = p
        self.matrix = []
        for i in range(5):
            self.matrix.append(['', '', '', '', ''])
        self.encrypt(key)

    def encrypt(self, key):
        key = key.lower()
        self.construct_matrix(key)
        cipher = open('playfair_cipher.txt', 'w')
        cipherText = ''
        for line in self.plainText:
            if line == '':
                continue
            line = line.lower()
            p = self.handle(line)
            c = ''
            for i in range(0, len(p) - 1, 2):
                x = self.position(p[i])
                y = self.position(p[i + 1])
                if x[0] == y[0]:
                    c += self.matrix[x[0]][(x[1] + 1) % 5]
                    c += self.matrix[y[0]][(y[1] + 1) % 5]
                elif x[1] == y[1]:
                    c += self.matrix[(x[0] + 1) % 5][x[1]]
                    c += self.matrix[(y[0] + 1) % 5][y[1]]
                else:
                    c += self.matrix[x[0]][y[1]]
                    c += self.matrix[y[0]][x[1]]
            cipherText += c
            cipherText += '\n'
        cipher.write(cipherText)

    def construct_matrix(self, key):
        ptr = 0
        alpha = 97
        key = key.lower()
        key = key.replace('j', 'i')
        key = "".join(OrderedDict.fromkeys(key))
        for i, j in product(range(5), range(5)):
            self.matrix[i][j] = key[ptr]
            ptr += 1
            if ptr == len(key):
                break

        for i, j in product(range(5), range(5)):
            while self.matrix[i][j] == '':
                if not self.isExist(chr(alpha)):
                    self.matrix[i][j] = chr(alpha)
                alpha += 1

    def isExist(self, char):
        for i in range(5):
            if char in self.matrix[i]:
                return True
            if char == 'j':
                if 'i' in self.matrix[i]:
                    return True
            if char == 'i':
                if 'j' in self.matrix[i]:
                    return True
        return False

    def position(self, char):
        for i, j in product(range(5), range(5)):
            if char == self.matrix[i][j]:
                return [i, j]
            if char == 'i' and self.matrix[i][j] == 'j':
                return [i, j]
            if char == 'j' and self.matrix[i][j] == 'i':
                return [i, j]

    def handle(self, str):
        x = str[0]
        for i in range(1, len(str)):
            if str[i] != x[-1]:
                x += str[i]
            else:
                x = x + 'x' + str[i]

        if len(x) % 2 == 1:
            x += 'x'
        return x
