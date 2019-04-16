import re

def isValidEmail(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def isValidPhone(phone):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    parts = phone.split('-')
    if len(parts) != 3:
        return False

    if len(parts[0]) == 3:
        for s in parts[0]:
            if s not in nums:
                return False
    else:
        return False

    if len(parts[1]) == 3:
        for s in parts[1]:
            if s not in nums:
                return False
    else:
        return False

    if len(parts[2]) == 4:
        for s in parts[2]:
            if s not in nums:
                return False
        return True
    else:
        return False

def isValidZipcode(zipcode):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    if len(zipcode) == 9:
        for s in zipcode:
            if s not in nums:
                return False
        return True
    else:
        return False

print(isValidPhone('123-123-1234'))
print(isValidPhone('123-123-123'))
print(isValidPhone('123-11223-1234'))