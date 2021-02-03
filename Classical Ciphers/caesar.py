class CaesarCipher:
    def __init__(self, p, key):
        self.plainText = p
        self.encrypt(key)

    def encrypt(self, key):
        cipher = open('caesar_cipher.txt', 'w')
        cipherText = ''
        for line in self.plainText:
            if line == '':
                continue
            line = line.lower()
            c = ''
            for i in range(len(line)):
                c += chr(((ord(line[i]) - 97 + key) % 26) + 97)
            cipherText += c
            cipherText += '\n'
        cipher.write(cipherText)
