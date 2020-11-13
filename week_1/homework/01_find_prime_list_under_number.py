input = 20


def find_prime_list_under_number(number):
    array = []

    if number <= 1:
        return "입력값을 2이상으로 수정해주세요."
    for i in range(2,number+1):
        temp = 1
        for j in range(2, i):
            if i % j ==0:
                temp = 0
                break
        if temp == 1:
            array.append(i)
    return array


result = find_prime_list_under_number(input)
print(result)
