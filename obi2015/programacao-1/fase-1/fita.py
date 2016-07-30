if __name__ == '__main__':
    n = int(input())
    f = ''.join((x if x == '0' else 'x' for x in input().split()))
    result = ''
    for x in range(n):
        if f[x] is '0':
            result += '0 '
            continue
        before = f.rfind('0', 0, x)
        after = f.find('0', x, n)
        if before >= 0 and after >= 0:
            if x - before > after - x:
                result += str(after - x)
            else:
                result += str(x - before)
        elif before >= 0:
            result += str(x - before)
        else:
            result += str(after - x)
        result += ' '

    print(result.strip())
