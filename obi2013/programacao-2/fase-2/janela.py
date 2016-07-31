# status: testado com exemplos da prova

if __name__ == '__main__':
    f1, f2, f3 = sorted([int(x) for x in input().split(' ')])

    HEIGHT = 100
    WINDOW_WIDTH = 600
    PIECE_WIDTH = 200

    piece_1 = (f1, f1 + PIECE_WIDTH)
    piece_2 = (f2, f2 + PIECE_WIDTH)
    piece_3 = (f3, f3 + PIECE_WIDTH)

    open_area = WINDOW_WIDTH * HEIGHT

    open_area -= (piece_1[1] - piece_1[0]) * HEIGHT

    if piece_2[0] < piece_1[1]:
        open_area -= (piece_2[1] - piece_1[1]) * HEIGHT
    else:
        open_area -= (piece_2[1] - piece_2[0]) * HEIGHT

    if piece_3[0] <= piece_2[1]:
        open_area -= (piece_3[1] - piece_2[1]) * HEIGHT
    else:
        open_area -= (piece_3[1] - piece_3[0]) * HEIGHT

    print(open_area)
