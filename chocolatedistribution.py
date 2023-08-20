"""Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum."""
def distributeChocolates(A, N, M):
    A.sort()
    min_diff = float('inf')
    start_index = 0

    for i in range(N - M + 1):
        diff = A[i + M - 1] - A[i]
        if diff < min_diff:
            min_diff = diff
            start_index = i

    return A[start_index:start_index + M]
