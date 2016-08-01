# status: testado com exemplos da prova
import math

if __name__ == '__main__':
    C, T = map(int, input().split())
    radiuses = []
    shots = []
    points = 0

    for x in range(C):
        radiuses.append(int(input()))

    for x in range(T):
        shots.append([float(x) for x in input().split()])

    for x, y in shots:
        hypotenuse = math.hypot(x, y)

        for index in range(C):
            if hypotenuse <= radiuses[index]:
                points += C - index
                break

    print(points)
