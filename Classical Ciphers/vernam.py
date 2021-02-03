class VernamCipher:
    def __init__(self, p, key):
        self.plainText = p
        self.encrypt(key)

    def encrypt(self, key):
        cipher = open('vernam_cipher.txt', 'w')
        cipherText = ''
        key = key.lower()
        for line in self.plainText:
            if line == '':
                continue
            line = line.lower()
            c = ''
            for i in range(len(line)):
                c += chr(((ord(line[i]) - 97 + ord(key[i]) - 97) % 26) + 97)
            cipherText += (c + '\n')
        cipher.write(cipherText)
