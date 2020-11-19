finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    arr = sorted(numbers)
    minimum = 0
    maximum = len(arr) -1
    mid = (minimum + maximum)//2

    while minimum <= maximum:
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            minimum = mid + 1
        else:
            maximum = mid - 1
        mid = (minimum + maximum) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)