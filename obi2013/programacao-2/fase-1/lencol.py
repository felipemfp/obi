# status: testado com exemplos da prova

if __name__ == '__main__':
    a1, b1, a2, b2, a, b = map(int, input().split())

    if a1 * b1 + a2 * b2 >= a * b:
        print('S')
    else:
        print('N')
