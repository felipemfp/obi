# status: testado com exemplos da prova

if __name__ == '__main__':
    stickes = [int(x) for x in input().split(' ')]

    can = False

    groups = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

    for g in groups:
        if stickes[g[0]] < stickes[g[1]] + stickes[g[2]] and \
                stickes[g[1]] < stickes[g[0]] + stickes[g[2]] and \
                stickes[g[2]] < stickes[g[1]] + stickes[g[0]]:
            can = True
            break

    print('S' if can else 'N')
