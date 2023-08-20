def product_except_self(nums):
    n = len(nums)
    left_product = [1] * n
    right_product = [1] * n
    result = [1] * n

    # Calculate left_product array
    left = 1
    for i in range(n):
        left_product[i] = left
        left *= nums[i]

    # Calculate right_product array
    right = 1
    for i in range(n - 1, -1, -1):
        right_product[i] = right
        right *= nums[i]

    # Construct the product array P
    for i in range(n):
        result[i] = left_product[i] * right_product[i]

    return result

# Example usage
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print("Product array P:", result)  # Output: [24, 12, 8, 6]
