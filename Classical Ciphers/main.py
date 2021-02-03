from caesar import CaesarCipher
from playfair import PlayFairCipher
from hill import HillCipher
from vigenere import VigenereCipher
from vernam import VernamCipher

# Caesar cipher algorithm takes input from caesar_plain.txt and output the cipher text to caesar_cipher.txt
# the CaesarCipher class constructor takes the plainText and the key
# Testing with key = 3 if you want to change the key, pass another key to the class constructor
caesarPlain = open('caesar_plain.txt', 'r').read().split('\n')
caesar = CaesarCipher(caesarPlain, 3)

# PlayfairCipher
playfairPlain = open('playfair_plain.txt', 'r').read().split('\n')
playfair = PlayFairCipher(playfairPlain, 'rats')

# HillCipher 2x2
hillPlain_2x2 = open('hill_plain_2x2.txt', 'r').read().split('\n')
hill_2x2 = HillCipher(hillPlain_2x2, [5, 17, 8, 3])

# HillCipher 3x3
hillPlain_3x3 = open('hill_plain_3x3.txt', 'r').read().split('\n')
hill_3x3 = HillCipher(hillPlain_3x3, [2, 4, 12, 9, 1, 6, 7, 5, 3])

# VigenereCipher auto mode
vigenereAutoPlain = open('vigenere_plain.txt', 'r').read().split('\n')
vigenereAuto = VigenereCipher(vigenereAutoPlain, 'aether', 1)

# VigenereCipher repeating mode
vigenereRepeatingPlain = open('vigenere_plain.txt', 'r').read().split('\n')
vigenereRepeating = VigenereCipher(vigenereRepeatingPlain, 'pie', 0)

# VernamCipher
vernamPlain = open('vernam_plain.txt', 'r').read().split('\n')
vernam = VernamCipher(vernamPlain, 'SPARTANS')
