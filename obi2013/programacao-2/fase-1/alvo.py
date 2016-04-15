# status: testado com exemplos da prova
def teste(n):
    return 0


import math

if __name__ == '__main__':
    C, T = map(int, input().split(' '))
    radiuses = []
    shots = []
    points = 0

    for x in range(C):
        radiuses.append(int(input().strip()))

    for x in range(T):
        shots.append([float(x) for x in input().strip().split(' ')])

    for x, y in shots:
        hypotenuse = math.hypot(x, y)

        for index in range(len(radiuses)):
            if hypotenuse <= radiuses[index]:
                points += len(radiuses) - index
                break

    print(points)
