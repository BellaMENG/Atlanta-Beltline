import re
import base64

def encodeStr(s):
    return base64.b64encode(s.encode('utf-8'))

def decodeStr(b):
    # print(b)
    # print(type(b))
    b = str.encode(b)
    # print(type(b))
    # print(b[2:-1])
    return base64.b64decode(b[2:-1]).decode('utf-8')

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
    if len(zipcode) == 5:
        for s in zipcode:
            if s not in nums:
                return False
        return True
    else:
        return False

import hashlib, binascii, os

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    #print(provided_password)
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    #print(pwdhash)
    return pwdhash == stored_password

#print(len(hash_password("qwueydjclvkvjsiflmcps")))