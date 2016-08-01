# status: testado com exemplos da prova

if __name__ == '__main__':
    album = sorted([int(x) for x in input().split()])
    square_1 = sorted([int(x) for x in input().split()])
    square_2 = sorted([int(x) for x in input().split()])
    fits = False

    if album[0] >= square_1[1] and album[0] >= square_2[1]:
        if album[1] >= square_1[0] + square_2[0]:
            fits = True
    if album[1] >= square_1[0] and album[1] >= square_2[0]:
        if album[0] >= square_1[1] + square_2[1]:
            fits = True

    print('S' if fits else 'N')
