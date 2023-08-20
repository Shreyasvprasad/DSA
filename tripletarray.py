"""Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X."""
def findTriplet(arr, X):
    arr.sort()

    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]

            if curr_sum == X:
                return True
            elif curr_sum < X:
                left += 1
            else:
                right -= 1

    return False
