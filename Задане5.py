from xmlrpc.client import MAXINT, MININT
def func1(number):
    str_number = str(number)
    a = 0
    b = MAXINT
    c = MININT
    d = 0
    result = ''
    for i in str_number:
        if int(i) % 2 == 0:
            a += int(i)
        if b > int(i):
            b = int(i)
        if c < int(i):
            c = int(i)
        d = (c - b) ** 3
    a = a ** 2
    if a > d:
        return f'{d}{a}'
    else:
        return f'{a}{d}'


i = 0
j = 0
print (func1(12))
while i != 14:
    i = func1(j)
    j += 1

print(j)
