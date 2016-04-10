# status: testado com exemplos da prova

if __name__ == '__main__':
    n1, d1, v1 = map(int, input().split(' '))
    n2, d2, v2 = map(int, input().split(' '))

    time1 = d1 / v1
    time2 = d2 / v2

    if time1 < time2:
        print(n1)
    else:
        print(n2)
