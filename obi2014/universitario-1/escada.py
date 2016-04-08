# status: testada com exemplos da prova

if __name__ == '__main__':
    size = input().strip().split(' ')
    row, column = int(size[0]), int(size[-1])
    rows = []
    for x in range(0, row):
        rows.append(input().strip())

    result = 'S'
    first_not_zero = None
    only_zero = False
    for r in rows:
        chars = [int(c) for c in r.split(' ')]

        if only_zero:
            if any(chars):
                result = 'N'
                break

        if first_not_zero is not None:
            if chars[first_not_zero]:
                result = 'N'
                break
            elif first_not_zero > 0 and chars[first_not_zero - 1]:
                result = 'N'
                break

        if any(chars):
            for y in range(0, len(chars)):
                if chars[y]:
                    first_not_zero = y
                    break
        else:
            only_zero = True

    print(result)
