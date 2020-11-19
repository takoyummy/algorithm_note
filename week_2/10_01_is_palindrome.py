input = "abcba"


def is_palindrome(string):
    first = 0
    last = len(string) - 1
    while first < last:
        if string[first] == string[last]:
            first += 1
            last -= 1
        else:
            return False

    return True


print(is_palindrome(input))