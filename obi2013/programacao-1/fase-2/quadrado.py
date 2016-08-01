# status: testado com exemplos da prova

if __name__ == '__main__':
    n = int(input())
    cubes = [int(x) for x in input().split()]

    ways = 0

    for x in range(0, n):
        x_sum = cubes[x]
        for y in range(x, n):
            if x == y:
                if cubes[y] % 8 == 0:
                    ways += 1
            else:
                x_sum += cubes[y]
                if x_sum % 8 == 0:
                    ways += 1

    print(ways)
