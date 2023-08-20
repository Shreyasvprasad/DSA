def can_cut_trees(heights, n, M, H):
    wood_cut = 0
    for height in heights:
        if height > H:
            wood_cut += height - H
    return wood_cut >= M

def find_maximum_sawblade_height(heights, n, M):
    low = 1
    high = max(heights)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_cut_trees(heights, n, M, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# Example usage
n, M = map(int, input().split())
heights = list(map(int, input().split()))
result = find_maximum_sawblade_height(heights, n, M)
print(result)
