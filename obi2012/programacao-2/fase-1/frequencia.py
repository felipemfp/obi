# status: testado com exemplos da prova

if __name__ == '__main__':
    N = int(input().strip())

    registers = set()

    for x in range(N):
        registers.add(int(input().strip()))

    print(len(registers))
