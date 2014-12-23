#/usr/bin/python

N = 10000
cache = {}

def is_palindrome(n):
    s = str(n)
    return all(s[i] == s[len(s) - 1 - i] for i in range(0, (len(s) / 2)))

def lychrel(n):
    if n in cache:
        return cache[n]
    else:
        new_n = n + int(''.join(reversed(str(n))))
        cache[n] = is_lychrel(new_n, 0)
        return cache[n]

def is_lychrel(n, cnt):
    if cnt > 50:
        return True
    elif is_palindrome(n):
        return False

    if n in cache:
        return cache[n]

    n += int(''.join(reversed(str(n))))
    return is_lychrel(n, cnt+1)


result = [n for n in range(N+1) if lychrel(n)]
print len(result)

