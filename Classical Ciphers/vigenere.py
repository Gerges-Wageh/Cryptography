class VigenereCipher:
    def __init__(self, p, key, mode):
        self.plainText = p
        self.encrypt(key, mode)

    def encrypt(self, key, mode):
        cipherText = ''
        key = key.lower()
        for line in self.plainText:
            if line == '':
                continue
            line = line.lower()
            if mode == 1:
                cipherText += (self.auto(key, line) + '\n')
            else:
                cipherText += (self.repeating(key, line) + '\n')
        if mode == 1:
            cipher = open('vigenere_cipher_auto.txt', 'w')
            cipher.write(cipherText)
        else:
            cipher = open('vigenere_cipher_repeating.txt', 'w')
            cipher.write(cipherText)


    def auto(self, key, text):
        c = ''
        ptr = 0
        while len(key) < len(text):
            key += text[ptr]
            ptr += 1
        for i in range(len(key)):
            c += chr(((ord(text[i]) - 97 + ord(key[i]) - 97) % 26) + 97)
        return c

    def repeating(self, key, text):
        temp = key
        c = ''
        while len(key) < len(text):
            key += temp
        key = key[:len(text)]
        for i in range(len(key)):
            c += chr(((ord(text[i]) - 97 + ord(key[i]) - 97) % 26) + 97)
        return c
