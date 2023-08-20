"""Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray."""
def maxProductSubarray(Arr):
    if len(Arr) == 0:
        return 0

    max_product = 1
    min_product = 1
    result = float('-inf')

    for num in Arr:
        if num == 0:
            max_product = 1
            min_product = 1
        elif num > 0:
            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)
        else:
            max_product, min_product = max(num, num * min_product), min(num, num * max_product)

        result = max(result, max_product)

    return result
