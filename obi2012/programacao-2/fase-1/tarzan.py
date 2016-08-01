# status: testado com exemplos da prova

import math

if __name__ == '__main__':
    N, D = (int(x) for x in input().split())

    trees = []
    possible_trees = set()

    for x in range(N):
        trees.append(tuple([int(x) for x in input().split()]))

    for x in range(N):
        for y in range(N):
            if x == y:
                continue
            X, Y = trees[x][0] - trees[y][0], trees[x][1] - trees[y][1]
            if math.hypot(X, Y) <= D:
                possible_trees.add(trees[y])

    print('S' if len(possible_trees) == len(trees) else 'N')
