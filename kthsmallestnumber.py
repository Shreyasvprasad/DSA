def find_kth_smallest(ranges, k):
    merged = []
    for a, b in ranges:
        merged.append((a, 1))  # '1' indicates the start of a range
        merged.append((b, 0))  # '0' indicates the end of a range
    
    merged.sort()  # Sort the ranges and endpoints
    
    count = 0
    prev = None
    for num, flag in merged:
        if flag == 1:
            count += 1
        if count >= k:
            return num
        if flag == 0:
            count -= 1
        prev = num
    
    return prev + k - count

def main():
    T = int(input())
    for _ in range(T):
        N, Q = map(int, input().split())
        ranges = []
        for _ in range(N):
            A, B = map(int, input().split())
            ranges.append((A, B))
        for _ in range(Q):
            K = int(input())
            result = find_kth_smallest(ranges, K)
            print(result)

if __name__ == "__main__":
    main()
