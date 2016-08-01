# status: testado com exemplos da prova

if __name__ == '__main__':
    text = input()
    pieces = text.split()
    nice_pieces = [x[1::2] for x in pieces]
    print(' '.join(nice_pieces))
