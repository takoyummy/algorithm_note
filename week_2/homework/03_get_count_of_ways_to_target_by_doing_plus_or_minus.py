numbers = [1, 1, 1, 1, 1]
target_number = 3
count = 0


# 재귀 어려워욥
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, index, sum):
    if index == len(numbers):
        if sum == target:
            global count
            count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, index + 1, sum + numbers[index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, index + 1, sum - numbers[index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(count)
