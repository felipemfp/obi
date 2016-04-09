# status: testado com exemplos da prova

def input_to_minutes(value):
    h, m = (int(v) for v in value.split(':'))
    return h * 60 + m

if __name__ == '__main__':
    values = [input_to_minutes(v) for v in input().strip().split(' ')]
    minutes_a_to_b = values[1] - values[0]
    minutes_b_to_a = values[3] - values[2]

    duration = (minutes_a_to_b + minutes_b_to_a) / 2
    variation = (minutes_a_to_b - duration) / 60

    if duration < 0:
        minutes_a_to_b += 24 * 60

    duration = (minutes_a_to_b + minutes_b_to_a) / 2
    variation = (minutes_a_to_b - duration) / 60

    if variation > 12 :
        variation = variation - 12 + - 12
    elif variation < -12:
        variation = (variation * -1) - 12 + - 12

    print(int(duration), int(variation))
