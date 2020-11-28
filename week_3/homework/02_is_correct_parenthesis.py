s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    r =0
    if string[0] == ")" or None:
        return False

    for i in string:
        if i =="(":
            r += 1
        elif i == ")":
            r -= 1
    if r == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!