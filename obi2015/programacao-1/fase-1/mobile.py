if __name__ == '__main__':
    a, b, c, d = (int(input()) for x in range(4))

    if b == c and d == b + c and a == b + c + d:
        print('S')
    else:
        print('N')
