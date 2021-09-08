def is_palindrome(string):
    if string[::-1] == string:
        return True
    return False


is_palindrome("heeh")
