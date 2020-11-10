input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurence_array = [0] * 26
    for i in string:
        if i.isalpha():
            num = ord(i) - ord('a')
            alphabet_occurence_array[num] += 1

    for n in alphabet_occurence_array:
        for cpn in alphabet_occurence_array:
            if n < cpn:
                break
        return alphabet_occurence_array[n]



result = find_max_occurred_alphabet(input)
print(result)
