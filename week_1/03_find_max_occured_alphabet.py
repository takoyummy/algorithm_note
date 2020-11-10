def find_alphabet_occurrence_array(string):
    # 이 부분을 채워보세요!
    alphabet_occurence_array = [0] * 26
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" , "q", "r", "s", "t", "u", "v"," w", "x", "y", "z"]
    for i in string:
        if i.isalpha():
            num = ord(i) - ord('a')
            alphabet_occurence_array[num] += 1

    print(alphabet_occurence_array)
    # for n in alphabet_occurence_array:
    #     for cpn in alphabet_occurence_array:
    #         if n < cpn:
    #             break
    #     return alphabet_occurence_array[n]
    max = 0
    index = 0
    for n in alphabet_occurence_array:
        if alphabet_occurence_array[n] > max:
            index = n
    return alphabet[n]








print(find_alphabet_occurrence_array("hello my name is sparta"))
