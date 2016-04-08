# status: testada com exemplos da prova

if __name__ == '__main__':
    st_line = [int(x) for x in input().strip().split(' ')]
    nd_line = [int(x) for x in input().strip().split(' ')]
    rd_line = [int(x) for x in input().strip().split(' ')]

    houses = st_line[0]
    letters = st_line[-1]

    moves = 0

    last_house = 0
    for house in rd_line:
        in_houses = nd_line.index(house)
        if last_house > in_houses:
            moves += last_house - in_houses
        elif last_house < in_houses:
            moves += in_houses - last_house
        last_house = in_houses

    print(moves)
