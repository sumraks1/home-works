numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []

for i in range(2, 16):
    for j in range(2, 16):
        f'{i / j }'
    is_prime = True
    if is_prime == i // j:
        primes.append(i)
    elif is_prime != i // j:
        not_primes.append(i)
print(primes)
print(not_primes)