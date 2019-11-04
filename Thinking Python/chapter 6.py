def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

def ack_memo(m, n):
    cache = {}

    if m == 0:
        return n+1
    if n == 0:
        return ack_memo(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ack_memo(m-1, ack_memo(m, n-1))
        return cache[m, n]

def is_palindrome(word):
    return word == word[::-1]


def is_power(a, b):
    if a % b == 0:
        if a == b:
            return True
        else:
            return is_power(a/b, b)
    return False


def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(b % a, a)

print(ack(3, 4))
print(ack_memo(3, 6))
print(is_palindrome('anna'), is_palindrome('kostya'))
print(is_power(5000, 2))
print(gcd(98, 56))
