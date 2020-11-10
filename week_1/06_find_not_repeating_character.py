input = "abacabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurence_array = [0] * 26

    for i in string:
        alphabet_occurence_array[ord(i) - ord("a")] += 1

    for i in string:
        n = ord(i) - ord("a")
        if alphabet_occurence_array[n] == 1:
            return chr(n + ord('a'))
    return "_"





result = find_not_repeating_character(input)
print(result)
