# status: testado com exemplos da prova

if __name__ == '__main__':
    N = int(input().strip())

    registers = []

    for x in range(N):
        registers.append(int(input().strip()))

    print(len(set(registers)))
