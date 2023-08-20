def min_flips_to_alternate(binary_string):
    count_starting_with_0 = 0
    count_starting_with_1 = 0
    
    for i, bit in enumerate(binary_string):
        if i % 2 == 0:
            if bit == '1':
                count_starting_with_0 += 1
            else:
                count_starting_with_1 += 1
        else:
            if bit == '0':
                count_starting_with_0 += 1
            else:
                count_starting_with_1 += 1
    
    return min(count_starting_with_0, count_starting_with_1)

# Example usage
binary_str = "010101"
result = min_flips_to_alternate(binary_str)
print("Minimum flips:", result)  # Output: 2
