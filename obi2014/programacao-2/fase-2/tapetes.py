# status: testado com exemplos da prova

if __name__ == '__main__':
    length, count = [int(x) for x in input().strip().split(' ')]

    rug_1 = count - 1
    rug_max = length - rug_1

    print(rug_max**2 + rug_1)
