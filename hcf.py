def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 60
result_hcf = hcf(num1, num2)
print(f"HCF of {num1} and {num2} is {result_hcf}")
