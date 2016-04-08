# status: testada com exemplos da prova

def is_open(pins, ideal_height):
    for pin in pins:
        if pin != ideal_height:
            return False
    return True

def right_or_left(pins, index, ideal_height):
    left, right = index - 1, index + 1
    if pins[left] < pins[right] and pins[left] != ideal_height:
        return left
    return right


if __name__ == '__main__':
    pins_count, ideal_height = (int(v) for v in input().strip().split(' '))
    pins = [int(v) for v in input().strip().split(' ')]

    moves = 0

    while not is_open(pins, ideal_height):
        ind = pins.index(sorted([p for p in pins if p != ideal_height])[0]);
        pin = pins[ind]
        pin_right = pins[ind + 1] if ind < len(pins) - 1 else None
        pin_left = pins[ind - 1] if ind > 0 else None

        required_moves = ideal_height - pin
        if pin_left is None or (pin_right is not None and pin_right < pin_left and pin_right != ideal_height) or (pin_left == ideal_height and pin_right is not None):
            expected_pin_right = pin_right + required_moves
            if required_moves > 0:
                if expected_pin_right > ideal_height:
                    required_moves -= expected_pin_right - ideal_height
            else:
                if expected_pin_right < ideal_height:
                    required_moves += ideal_height - expected_pin_right
            if required_moves == 0:
                required_moves = ideal_height - pin
            pins[ind + 1] += required_moves
        elif pin_left is not None:
            expected_pin_left = pin_left + required_moves
            if required_moves > 0:
                if expected_pin_left > ideal_height:
                    required_moves -= expected_pin_left - ideal_height
            else:
                if expected_pin_left < ideal_height:
                    required_moves += ideal_height - expected_pin_left
            if required_moves == 0:
                required_moves = ideal_height - pin
            pins[ind - 1] += required_moves
        pins[ind] += required_moves
        moves += required_moves if required_moves >= 0 else required_moves * -1

    print(moves)
