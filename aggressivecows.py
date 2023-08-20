def is_possible(stalls, n, cows, min_distance):
    count = 1
    last_position = stalls[0]
    
    for i in range(1, n):
        if stalls[i] - last_position >= min_distance:
            count += 1
            last_position = stalls[i]
            if count == cows:
                return True
    
    return False

def largest_minimum_distance(stalls, n, cows):
    stalls.sort()
    low = 0
    high = stalls[-1] - stalls[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(stalls, n, cows, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# Example usage
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n, c = map(int, input().split())
    stall_positions = []
    for _ in range(n):
        stall_positions.append(int(input()))
    result = largest_minimum_distance(stall_positions, n, c)
    print(result)
