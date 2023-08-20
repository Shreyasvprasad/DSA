def find_min_max(arr):
    n = len(arr)
    
    if n == 1:
        return arr[0], arr[0]

    # Initialize min and max variables to compare elements
    if n % 2 == 0:
        if arr[0] < arr[1]:
            min_val = arr[0]
            max_val = arr[1]
        else:
            min_val = arr[1]
            max_val = arr[0]
