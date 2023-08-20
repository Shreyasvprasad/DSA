def roman_to_int(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for symbol in reversed(s):
        value = roman_values[symbol]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

# Example usage
roman_numeral = "MCMXCIV"
integer_value = roman_to_int(roman_numeral)
print("Integer value:", integer_value)  # Output: 1994
