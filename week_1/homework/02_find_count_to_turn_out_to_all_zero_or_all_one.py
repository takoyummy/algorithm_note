input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    zero2one = 0
    one2zero = 0
    if string[0] == "0":
        zero2one = 1
    if string[0] == "1":
        one2zero = 1

    for i in range(len(string)-1):
        if string[i] != string[i + 1]:
            if string[i + 1] == "1":
                one2zero += 1
            if string[i + 1] == "0":
                zero2one += 1
    return min(one2zero,zero2one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
