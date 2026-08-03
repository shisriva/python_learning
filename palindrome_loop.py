'''
Write is_palindrome(s) that returns True if the string reads the same forwards and backwards (ignore case).

'''

def is_palindrome(s):
    s = s.lower()
    reversed_text = ""

    for alpha in s:
        reversed_text = alpha + reversed_text

    return reversed_text == s


# try
print(is_palindrome("Level"))   # True
print(is_palindrome("hello"))   # False
print(is_palindrome("madam"))   # True
