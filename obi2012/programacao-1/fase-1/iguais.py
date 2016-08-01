# status: testado com exemplos da prova

if __name__ == '__main__':
    N = input()
    values = [int(x) for x in input().split()]

    max_record = 0
    last_record = 0
    last_value = 0

    for value in values:
        last_record += 1
        if not value == last_value:
            last_record = 1
        max_record = last_record if last_record > max_record else max_record
        last_value = value

    print(max_record)
