def palindrome(letters):

    letters = list(filter(str.isalpha, str(letters).lower()))
    length = len(letters)
    if length <= 1:
        return True
    else:
        return (letters[0] == letters[-1]) and palindrome(letters[1:-1])

print(palindrome(""))
