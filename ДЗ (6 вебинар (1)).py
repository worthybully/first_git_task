def palindrome(s):
    s_new = s.replace(' ', '')
    rev = s_new[::-1]
    if s_new == rev:
        return True
    return False