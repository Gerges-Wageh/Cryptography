class DES:
    def encrypt(self, key, plainText, n):
        shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        plainText = self.toBinary(plainText)
        key = self.toBinary(key)
        keySeed = self.permutedChoice_1(key)
        p = self.IP(plainText)
        l, r = p[:32], p[32:]
        for j in range(n):
            for i in range(16):
                k, keySeed = self.generateKey(keySeed, shift[i])
                l, r = self.DESRound(l, r, k)
            l, r = r, l
            cipher = self.inverse_IP(l + r)
        cipher = self.toHex(cipher)
        return cipher

    def decrypt(self, key, cipherText, n):
        shift = [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0]
        cipherText = self.toBinary(cipherText)
        key = self.toBinary(key)
        keySeed = self.permutedChoice_1(key)
        c = self.IP(cipherText)
        l, r = c[:32], c[32:]
        for j in range(n):
            for i in range(15, -1, -1):
                k, keySeed = self.generateKey(keySeed, shift[i])
                l, r = self.DESRound(l, r, k)
            l, r = r, l
            plain = self.inverse_IP(l + r)
        plain = self.toHex(plain)
        return plain

    def toBinary(self, hex_16):
        bin_64 = ''
        for i in range(16):
            bin_64 += "{0:04b}".format(int(hex_16[i], 16))
        return bin_64

    def IP(self, x):
        table = [58, 50, 42, 34, 26, 18, 10, 2,
                 60, 52, 44, 36, 28, 20, 12, 4,
                 62, 54, 46, 38, 30, 22, 14, 6,
                 64, 56, 48, 40, 32, 24, 16, 8,
                 57, 49, 41, 33, 25, 17, 9, 1,
                 59, 51, 43, 35, 27, 19, 11, 3,
                 61, 53, 45, 37, 29, 21, 13, 5,
                 63, 55, 47, 39, 31, 23, 15, 7]
        op = ''
        for i in range(64):
            op += x[table[i] - 1]
        return op

    def inverse_IP(self, x):
        table = [40, 8, 48, 16, 56, 24, 64, 32,
                 39, 7, 47, 15, 55, 23, 63, 31,
                 38, 6, 46, 14, 54, 22, 62, 30,
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25]
        op = ''
        for i in range(64):
            op += x[table[i] - 1]
        return op

    def permutedChoice_1(self, x):
        table = [57, 49, 41, 33, 25, 17, 9,
                 1, 58, 50, 42, 34, 26, 18,
                 10, 2, 59, 51, 43, 35, 27,
                 19, 11, 3, 60, 52, 44, 36,
                 63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                 14, 6, 61, 53, 45, 37, 29,
                 21, 13, 5, 28, 20, 12, 4]
        op = ''
        for i in range(56):
            op += x[table[i] - 1]
        return op

    def permutedChoice_2(self, x):
        table = [14, 17, 11, 24, 1, 5, 3, 28,
                 15, 6, 21, 10, 23, 19, 12, 4,
                 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32]

        op = ''
        for i in range(48):
            op += x[table[i] - 1]
        return op

    def expansionPermutation(self, x):
        table = [32, 1, 2, 3, 4, 5,
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]
        op = ''
        for i in range(48):
            op += x[table[i] - 1]
        return op

    def permutation(self, x):
        table = [16, 7, 20, 21, 29, 12, 28, 17,
                 1, 15, 23, 26, 5, 18, 31, 10,
                 2, 8, 24, 14, 32, 27, 3, 9,
                 19, 13, 30, 6, 22, 11, 4, 25]
        op = ''
        for i in range(32):
            op += x[table[i] - 1]
        return op

    def circularShitLeft(self, x, d, N):
        n = int(x, 2)
        x = ((n << d) % (1 << N)) | (n >> (N - d))
        return "{0:028b}".format(int(x))

    def circularShiftRight(self, x, d):
        n = int(x, 2)
        x = (n >> d) | (n << (28 - d)) & 0xFFFFFFFF
        return "{0:028b}".format(int(x))

    def xor(self, str1, str2, n):
        op = ''
        for i in range(n):
            if str1[i] == str2[i]:
                op += '0'
            else:
                op += '1'
        return op

    def generateKey(self, x, n):
        l, r = self.circularShitLeft(x[:28], n, 28), self.circularShitLeft(x[28:], n, 28)
        nextRoundSeed = l + r
        key = self.permutedChoice_2(nextRoundSeed)
        return key, nextRoundSeed

    def S_Box(self, x):
        S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
              ]
        S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
              ]
        S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
              ]
        S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
              ]
        S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
              ]
        S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
              ]
        S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
              ]
        S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
              ]
        p1, p2, p3, p4, p5, p6, p7, p8 = x[0:6], x[6:12], x[12:18], x[18:24], x[24:30], x[30:36], x[36:42], x[42:]
        op = ''
        op += "{0:04b}".format(int(S1[int(p1[0] + p1[5], 2)][int(p1[1:5], 2)]))
        op += "{0:04b}".format(int(S2[int(p2[0] + p2[5], 2)][int(p2[1:5], 2)]))
        op += "{0:04b}".format(int(S3[int(p3[0] + p3[5], 2)][int(p3[1:5], 2)]))
        op += "{0:04b}".format(int(S4[int(p4[0] + p4[5], 2)][int(p4[1:5], 2)]))
        op += "{0:04b}".format(int(S5[int(p5[0] + p5[5], 2)][int(p5[1:5], 2)]))
        op += "{0:04b}".format(int(S6[int(p6[0] + p6[5], 2)][int(p6[1:5], 2)]))
        op += "{0:04b}".format(int(S7[int(p7[0] + p7[5], 2)][int(p7[1:5], 2)]))
        op += "{0:04b}".format(int(S8[int(p8[0] + p8[5], 2)][int(p8[1:5], 2)]))

        return op

    def toHex(self, x):
        op = ''
        for i in range(0, 64, 4):
            op += hex(int(x[i:i + 4], 2))[2:].upper()
        return op

    def DESRound(self, left, right, key):
        R_op = self.expansionPermutation(right)
        R_op = self.xor(R_op, key, 48)
        R_op = self.S_Box(R_op)
        R_op = self.permutation(R_op)
        R_op = self.xor(R_op, left, 32)
        left = right
        right = R_op
        return left, right


Algorithm = DES()
while 1:
    print('>>>>> Encrypt|Decrypt  0|1 <<<<<')
    mode = input('Please select the mode: ')
    if mode == '0':
        key = input('Please enter the key: ')
        plain = input('Please enter the plainText: ')
        n = int(input('number of runs: '))
        print('The cipherText: ', Algorithm.encrypt(key, plain, n))
    elif mode == '1':
        key = input('Please enter the key: ')
        cipher = input('Please enter the cipherText: ')
        n = int(input('number of runs: '))
        print('The plainText: ', Algorithm.decrypt(key, cipher, n))
    else:
        print('Invalid choice please try again!')
    print('\n')
