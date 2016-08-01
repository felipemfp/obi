# status: testado com exemplos da prova

if __name__ == '__main__':
    size, count_commands = (int(c) for c in input().split())

    commands = []

    for x in range(0, count_commands):
        commands.append([int(c) for c in input().split()])

    board = {}

    for x in range(0, size):
        for y in range(0, size):
            board[x, y] = 0

    for command in commands:
        if command[0] == 1:
            for x in range(0, size):
                board[command[1] - 1, x] = command[2]
        elif command[0] == 2:
            for x in range(0, size):
                board[x, command[1] - 1] = command[2]
        elif command[0] == 3:
            frequencies = {}
            for x in range(0, size):
                if not board[command[1] - 1, x] in frequencies.keys():
                    frequencies[board[command[1] - 1, x]] = 1
                else:
                    frequencies[board[command[1] - 1, x]] += 1
            print(sorted([x for x in frequencies.keys() if frequencies[
                  x] == max(frequencies.values())])[-1])
        elif command[0] == 4:
            frequencies = {}
            for x in range(0, size):
                if not board[x, command[1] - 1] in frequencies.keys():
                    frequencies[board[x, command[1] - 1]] = 1
                else:
                    frequencies[board[x, command[1] - 1]] += 1
            print(sorted([x for x in frequencies.keys() if frequencies[
                  x] == max(frequencies.values())])[-1])
