# status: testado com exemplos da prova

def look_for(list, x):
    for item in list:
        if item[0] == x:
            return item
    return None

if __name__ == '__main__':
    n = int(input().strip())
    highways = []

    for x in range(0, n):
        highways.append(input().strip().split(' '))

    initial = highways[0][0]
    result = True
    current = [initial,]

    while highways:
        if initial == current[-1] and len(current) == n:
            break
        else:
            highway = look_for(highways, current[-1])
            if highway == None:
                result = False
                break
            print(current[:1], highway)
            highways.remove(highway)
            current.append(highway[1])

    if result:
        print('S')
    else:
        print('N')
