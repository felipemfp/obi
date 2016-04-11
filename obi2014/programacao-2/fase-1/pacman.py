# status: testado com exemplos da prova

def walk(pacman, side):
    if pacman[0] % 2:
        if pacman[1] == 0:
            return pacman[0] + 1, pacman[1]
        return pacman[0], pacman[1] - 1
    else:
        if pacman[1] + 1 == side:
            return pacman[0] + 1, pacman[1]
        return pacman[0], pacman[1] + 1


if __name__ == '__main__':
    side = int(input().strip())
    rows = []

    for x in range(0, side):
        rows.append(input().strip())

    pacman = 0, 0
    max_fruits = 0
    fruits = 0

    while pacman[0] < side and pacman[1] < side:
        c = rows[pacman[0]][pacman[1]]
        if c == 'o':
            fruits += 1
        elif c == 'A':
            fruits = 0
        if fruits > max_fruits:
            max_fruits = fruits
        pacman = walk(pacman, side)

    print(max_fruits)
