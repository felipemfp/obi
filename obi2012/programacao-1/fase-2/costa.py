# status: testado com exemplos da prova


def is_coast(island, place):
    x, y = place[0], place[1]
    lines = len(island)
    columns = len(island[0])

    if island[x][y] == '#':
        if x == 0 or island[x - 1][y] == '.':
            return True
        elif y == columns - 1 or island[x][y + 1] == '.':
            return True
        elif x == lines - 1 or island[x + 1][y] == '.':
            return True
        elif y == 0 or island[x][y - 1] == '.':
            return True
    else:
        return False


if __name__ == '__main__':
    lines, columns = (int(x) for x in input().split())
    coasts = 0
    island = []
    for x in range(lines):
        island.append(input().strip())

    x = 0
    for line in island:
        for column in range(len(line)):
            if is_coast(island, (x, column)):
                coasts += 1
        x += 1
    print(coasts)
