def max_loot_amount(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    
    prev_loot = arr[0]
    curr_loot = max(arr[0], arr[1])
    
    for i in range(2, n):
        new_curr_loot = max(curr_loot, prev_loot + arr[i])
        prev_loot = curr_loot
        curr_loot = new_curr_loot
    
    return curr_loot

# Example usage
money_amounts = [6, 7, 1, 3, 8, 2, 4]
result = max_loot_amount(money_amounts)
print("Maximum money looted:", result)  # Output: 19 (7 + 3 + 8 + 4)
