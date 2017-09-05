
def is_possible(price, n, coins, total=0, index=0):
    if index >= n:
        return False
    total += coins[index]
    if total == price:
        return True
    if total < price:
        if is_possible(price, n, coins, total, index + 1):
            return True
    total -= coins[index]
    return is_possible(price, n, coins, total, index + 1)


if __name__ == '__main__':
    price, n = (int(x) for x in input().split())
    coins = [int(x) for x in input().split()]
    if is_possible(price, n, coins):
        print('S')
    else:
        print('N')
