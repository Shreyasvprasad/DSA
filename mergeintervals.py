"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input."""
def merge(intervals):
    # Sort the intervals based on starting point
    intervals.sort(key=lambda x: x[0])

    # Initialize result array with the first interval
    merged = [intervals[0]]

    # Iterate through the sorted intervals
    for interval in intervals[1:]:
        # Compare current interval with the last interval in the result array
        if interval[0] <= merged[-1][1]:  # Overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])  # Update ending point
        else:  # Non-overlapping intervals
            merged.append(interval)  # Add new interval to result array

    return merged
