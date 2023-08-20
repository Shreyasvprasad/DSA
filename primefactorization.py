def prime_factors_multiplicity(n):
    factors = []
    divisor = 2
    multiplicity = 0
    while n > 1:
        while n % divisor == 0:
            n //= divisor
            multiplicity += 1
        if multiplicity > 0:
            factors.append((divisor, multiplicity))
            multiplicity = 0
        divisor += 1
    return factors

num = int(input("Enter a number: "))
prime_factors = prime_factors_multiplicity(num)
print("Prime factors with multiplicity:", prime_factors)
