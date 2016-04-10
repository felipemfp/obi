# status: testado com exemplos da prova

def mover(tabela, linha, coluna):
    if not linha == 0:
        if tabela[linha - 1][coluna] == 1:
            return linha - 1, coluna
    if not coluna == len(tabela[0]) - 1:
        if tabela[linha][coluna + 1] == 1:
            return linha, coluna + 1
    if not linha == len(tabela) - 1:
        if tabela[linha + 1][coluna] == 1:
            return linha + 1, coluna
    if not coluna == 0:
        if tabela[linha][coluna - 1] == 1:
            return linha, coluna - 1
    return linha, coluna


if __name__ == '__main__':
    L, C = map(int, input().split(' '))
    il, ic = map(int, input().split(' '))
    il -= 1
    ic -= 1
    mapa = []

    for x in range(L):
        mapa.append([int(v) for v in input().split(' ')])

    chegou = False
    while not chegou:
        nl, nc = mover(mapa, il, ic)

        if nl == il and nc == ic:
            chegou = True
        else:
            mapa[il][ic] = 0
            il = nl
            ic = nc

    print(il + 1, ic + 1)
