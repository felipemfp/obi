# status: testado com exemplos da prova

parent = {}
size = {}

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def link(a, b):
    pa, pb = find(a), find(b)
    parent[pb] = pa
    if not pa in size.keys():
        size[pa] = size.get(pb, 0) + 1;
    else:
        size[pa] += size.get(pb, 0) + 1;

if __name__ == '__main__':
    n = int(input().strip())

    e = n * (n - 1) / 2

    for x in range(1, n + 1):
        parent[x] = x

    for x in range(0, n - 1):
        a, b, c = [int(x) for x in input().strip().split(' ')]
        if c == 0:
            link(a, b)

    for x in range(1, n + 1):
        if parent[x] == x:
            e -= size.get(x, 0) * (size.get(x, 0) + 1) / 2

    print(int(e))
