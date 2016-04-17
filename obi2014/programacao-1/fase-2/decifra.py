# status: testado com exemplos da prova

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

if __name__ == '__main__':
    cipher = input()
    text = input()

    message = ''

    for char in text:
        message += ALPHABET[cipher.index(char)]

    print(message)
