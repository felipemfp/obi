# status: testado com exemplos da prova

if __name__ == '__main__':
    N = int(input().strip())
    values = [int(x) for x in input().strip().split(' ')]

    for x in range(len(values)):
        if sum(values[:x]) == sum(values[x:]):
            print(x)
            break
