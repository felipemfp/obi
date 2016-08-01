# status: testado com exemplos da prova

if __name__ == '__main__':
    mattress_dimen = sorted([int(x) for x in input().split()])
    door_dimen = sorted([int(x) for x in input().split()])

    if mattress_dimen[0] <= door_dimen[0] and mattress_dimen[1] <= door_dimen[1]:
        print('S')
    else:
        print('N')
