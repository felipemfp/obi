# status: testado com exemplos da prova

def move(map, line, column):
    if not line == 0:
        if map[line - 1][column] == 1:
            return line - 1, column
    if not column == len(map[0]) - 1:
        if map[line][column + 1] == 1:
            return line, column + 1
    if not line == len(map) - 1:
        if map[line + 1][column] == 1:
            return line + 1, column
    if not column == 0:
        if map[line][column - 1] == 1:
            return line, column - 1
    return line, column


if __name__ == '__main__':
    L, C = map(int, input().split(' '))
    il, ic = map(int, input().split(' '))
    il -= 1
    ic -= 1
    map = []

    for x in range(L):
        map.append([int(v) for v in input().split(' ')])

    finished = False
    while not finished:
        nl, nc = move(map, il, ic)

        if nl == il and nc == ic:
            finished = True
        else:
            map[il][ic] = 0
            il = nl
            ic = nc

    print(il + 1, ic + 1)
