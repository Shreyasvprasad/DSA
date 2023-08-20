"""Given an large integer N, find its factorial. return a list of integers denoting the digits that make up the factorial of N."""
def factorialDigits(N):
    factorial = 1

    # Calculate the factorial of N
    for i in range(1, N + 1):
        factorial *= i

    # Convert the factorial into a list of digits
    digits = [int(digit) for digit in str(factorial)]

    return digits
