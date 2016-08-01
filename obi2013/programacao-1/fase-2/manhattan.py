# status: testado com exemplos da prova

if __name__ == '__main__':
    xm, ym, xr, yr = map(int, input().split())

    res_x = xr - xm if xr > xm else xm - xr
    res_y = yr - ym if yr > ym else ym - yr

    print(res_x + res_y)
