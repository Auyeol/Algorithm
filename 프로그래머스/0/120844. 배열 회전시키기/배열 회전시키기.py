def solution(numbers, direction):
    if direction == 'right':
        return [numbers.pop()] + numbers
    else:
        numbers.append(numbers[0])
        return numbers[1:]
    