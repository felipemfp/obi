# status: testado com exemplos da prova

import math

if __name__ == '__main__':
    N, D = [int(x) for x in input().strip().split(' ')]

    trees = []
    last_tree = []
    is_possible = True

    for x in range(N):
        trees.append([int(x) for x in input().strip().split(' ')])
        if x == 0:
            last_tree = trees[0]

    for tree in trees:
        X, Y = tree[0] - last_tree[0], tree[1] - last_tree[1]
        if math.hypot(X, Y) > D:
            is_possible = False
            break
        last_tree = tree

    print('S' if is_possible else 'N')
