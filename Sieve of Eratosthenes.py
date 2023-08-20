def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]

limit = int(input("Enter a limit: "))
prime_list = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, ":", prime_list)
