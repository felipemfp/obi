# status: testado com exemplos da prova

if __name__ == '__main__':
    len_a, len_b = [int(x) for x in input().strip().split(' ')]

    a = [int(x) for x in input().strip().split(' ')]
    b = [int(x) for x in input().strip().split(' ')]

    result = 'sim'

    for x in range(0, len_b):
        if b[x] in a:
            pass
        else:
            found = False
            for j in range(0, x):
                for k in range(0, x):
                    if b[j] + b[k] == b[x]:
                        found = True
                        break
                        break
            if not found:
                result = b[x]
                break

    print(result)
