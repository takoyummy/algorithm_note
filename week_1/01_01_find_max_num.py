input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    # max = 0
    # for i in range(len(array)):
    #     if input[i] > max:
    #         max = input[i]
    #
    #
    # return max

    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
