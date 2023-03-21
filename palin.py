palindrome.py
def palindrome(list):
    for i in len(list/2):
        if list[i] != list[len(list) - i]:
            return false
    return true
