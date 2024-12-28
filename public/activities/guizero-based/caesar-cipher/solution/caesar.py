NUM_LETTERS = 26

def encode_caesar(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                ciphertext += chr((ord(letter) + key - ord("A")) % NUM_LETTERS + ord("A"))
            else:
                ciphertext += chr((ord(letter) + key - ord("a")) % NUM_LETTERS + ord("a"))
        else:
            ciphertext += letter
    return ciphertext


def decode_caesar(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            if letter.isupper():
                plaintext += chr((ord(letter) - key - ord("A")) % NUM_LETTERS + ord("A"))
            else:
                plaintext += chr((ord(letter) - key - ord("a")) % NUM_LETTERS + ord("a"))
        else:
            plaintext += letter
    return plaintext
