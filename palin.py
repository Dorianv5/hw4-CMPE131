
def palindrome(list):
    for i in range(len(list) // 2):
        if list[i] != list[len(list) - i - 1]:
            return false
    return true
