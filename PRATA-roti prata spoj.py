def can_cook_pratas(pratas, cooks, mid):
    total_pratas = 0
    for cook in cooks:
        time_taken = 0
        pratas_cooked = 0
        while time_taken + (pratas_cooked + 1) * cook <= mid:
            pratas_cooked += 1
            time_taken += (pratas_cooked) * cook
        total_pratas += pratas_cooked
    return total_pratas >= pratas

def min_time_to_cook_pratas(pratas, cooks):
    low = 0
    high = 1e9
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if can_cook_pratas(pratas, cooks, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result

# Example usage
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    pratas = int(input())
    cooks = list(map(int, input().split()))
    l = cooks[0]
    cooks = cooks[1:]
    result = min_time_to_cook_pratas(pratas, cooks)
    print(result)
