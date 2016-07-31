# status: testado com exemplos da prova

tape = {}
days = 0

if __name__ == '__main__':
    length, n = (int(x) for x in input().split())
    seeds = (int(x) for x in input().split())

    for x in range(1, length + 1):
        tape[x] = 0

    for s in seeds:
        tape[s] = 1

    while not all(tape.values()):
        for s in [x for x in tape.keys() if tape[x]]:
            j = s - 1
            k = s + 1
            if j > 0:
                tape[j] = 1
            if k < length + 1:
                tape[k] = 1
        days += 1

    print(days)
