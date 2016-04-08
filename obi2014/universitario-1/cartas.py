# status: testada com exemplos da prova

if __name__ == '__main__':
    is_desc = False
    cards = input().strip().split(' ')
    if int(cards[0]) > int(cards[1]):
        is_desc = True

    result = ''
    for x in range(1, len(cards) - 1):
        if is_desc and int(cards[x]) < int(cards[x + 1]):
            result = 'N'
            break

        if not is_desc and int(cards[x]) > int(cards[x + 1]):
            result = 'N'
            break

    if result:
        pass
    elif is_desc:
        result = 'D'
    else:
        result = 'C'

    print(result)
