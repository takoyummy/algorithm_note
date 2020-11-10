input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result = 0



    for i in array:
        if result == 0:
            result = result + i
        elif i == 0 or i == 1:
            result += i
        else:
            result *= i
    return result



result = find_max_plus_or_multiply(input)
print(result)