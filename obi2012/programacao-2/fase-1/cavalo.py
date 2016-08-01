# status: testado com exemplos da prova


def move_piece(position, number):
    if number == 1:
        return position[0] + 1, position[1] + 2
    elif number == 2:
        return position[0] + 2, position[1] + 1
    elif number == 3:
        return position[0] + 2, position[1] - 1
    elif number == 4:
        return position[0] + 1, position[1] - 2
    elif number == 5:
        return position[0] - 1, position[1] - 2
    elif number == 6:
        return position[0] - 2, position[1] - 1
    elif number == 7:
        return position[0] - 2, position[1] + 1
    elif number == 8:
        return position[0] - 1, position[1] + 2


if __name__ == '__main__':
    moves_count = 0
    holes = [(1, 3),
             (2, 3),
             (2, 5),
             (5, 4)]
    horse_position = (4, 3)

    N = int(input().strip())
    moves = [int(x) for x in input().split()]

    for move in moves:
        moves_count += 1
        horse_position = move_piece(horse_position, move)
        if horse_position in holes:
            break

    print(moves_count)
