import re

def isValidEmail(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def isValidPhone(phone):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    if len(phone) == 9:
        for s in phone:
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

