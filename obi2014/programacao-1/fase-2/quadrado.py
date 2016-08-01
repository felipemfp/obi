# status: testado com exemplos da prova


def find_m(rows):
    result = {}
    for r in rows:
        if len(result.keys()) < 4:
            s = sum(r)
            if not s in result.keys():
                result[sum(r)] = 1
            else:
                result[sum(r)] += 1
        else:
            break
    mx = max(result.values())
    return sorted([x for x in result.keys() if result[x] == mx])[-1]


def find_wrong_row(rows, m):
    for x in range(0, len(rows)):
        if sum(rows[x]) != m:
            return x


def find_wrong_col(rows, m):
    ln = len(rows)
    for x in range(0, ln):
        s = 0
        for y in range(0, ln):
            s += rows[y][x]
        if s != m:
            return x


if __name__ == '__main__':
    n = int(input())
    rows = []
    for x in range(0, n):
        rows.append([int(x) for x in input().split()])

    m = find_m(rows)
    wrong_row = find_wrong_row(rows, m)
    wrong_col = find_wrong_col(rows, m)

    new_value = rows[wrong_row][wrong_col]
    old_value = m - (sum(rows[wrong_row]) - new_value)

    print(old_value, new_value)
