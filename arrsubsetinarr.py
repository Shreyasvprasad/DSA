"""Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. There can be duplicate elements.
 Create a hash set or a hash map to store the elements of array a1[].

Iterate through each element in array a2[].

Check if the current element exists in the hash set or hash map.

If it does not exist, return False as a2[] is not a subset of a1[].
If the iteration completes without returning False, it means that all elements of a2[] are present in a1[], so return True."""
def isSubset(a1, a2):
     set_a1 = set(a1)
 
     for num in a2:
         if num not in set_a1:
             return False
 
     return True
 