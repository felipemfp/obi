def combinations(lst, r):
    result = set()
    for x in range(r):
        a = tuple(lst[x:x + r])
        if len(a) == r:
            result.add(a)
    return result

if __name__ == '__main__':
    N, K = (int(x) for x in input().split())
    buildings = sorted([int(x) for x in input().split()])

    minor = buildings[-1] - buildings[0]

    for x in combinations(buildings, N - K):
        distance = x[-1] - x[0]
        if distance < minor:
            minor = distance

    print(minor)
