# status: testado com exemplos da prova

board = {}
track = {}
insecure_cells = 0


def walk(current):
    row, col = current[0], current[1]
    try:
        while not (row, col) in track[current]:
            track[current].append((row, col))
            if board[row, col] == 'A':
                row -= 1
            elif board[row, col] == 'V':
                row += 1
            elif board[row, col] == '>':
                col += 1
            elif board[row, col] == '<':
                col -= 1
    except:
        return False
    return True

if __name__ == '__main__':
    n = int(input())

    lines = []
    for x in range(0, n):
        lines.append(input())

    for x in range(0, n):
        for y in range(0, n):
            board[x, y] = lines[x][y]

    for k in board.keys():
        track[k] = []
        if walk(k) == False:
            insecure_cells += 1

    print(n**2 - insecure_cells)
