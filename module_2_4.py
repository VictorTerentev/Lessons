numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
"""for i in numbers:
    if i == 1:
        continue
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        primes.append(i)
    elif i == 2 or i == 3 or i == 5:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)
"""

for i in numbers:
    if i == 1:
        continue
    for j in range(2, 6):
        if i == j or i < j and i % 2 != 0:
            is_prime = True
            break
        elif i % j != 0:
            if i == j or i < j and i % 2 != 0:
                is_prime = True
                break
            is_prime = True
        else:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)