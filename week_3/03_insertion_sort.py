input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 이 부분을 채워보세요!
    for i in range(1, len(array)):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break

    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!