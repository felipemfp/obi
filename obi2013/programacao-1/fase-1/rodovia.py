# status: testado com exemplos da prova

if __name__ == '__main__':
    n = int(input())
    highways = []

    for x in range(n):
        highways.append([int(y) for y in input().split()])

    for x in range(1, n + 1):
        left = False
        arrive = False
        for y in highways:
            if y[0] == x:
                left = True
            if y[1] == x:
                arrive = True
            if left and arrive:
                break
        if not(left and arrive):
            print('N')
            exit()

    print('S')
