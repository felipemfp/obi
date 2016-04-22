# status: testado com exemplos da prova

if __name__ == '__main__':
    N = int(input().strip())
    houses = []
    for n in range(N):
        houses.append(int(input().strip()))
    K = int(input().strip())

    selected = []
    found = False

    for house in houses:
        for index in range(len(houses)):
            if house + houses[index] == K:
                selected = sorted([house, houses[index]])
                found = True
                break
        if found:
            print('{0} {1}'.format(selected[0], selected[1]))
            break
