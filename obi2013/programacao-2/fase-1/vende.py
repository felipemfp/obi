# status: testado com exemplos da prova

if __name__ == '__main__':
    N, K = [int(x) for x in input().strip().split(' ')]
    buildings = sorted([int(x) for x in input().strip().split(' ')])

    distance = buildings[-1]
    builds = 1
    max_builds = N - K
    last_build = 0
    last_distance = buildings[-1]

    for building in buildings:
        if building - last_build < last_distance and max_builds - 1 <= len(buildings) - buildings.index(building):
            distance = building - last_build
            builds = 1
        elif builds < max_builds - 1:
            distance += building - last_build
            builds += 1
        last_distance = building - last_build
        last_build = building

    print(distance)
