
"""Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.arr = [7, 10, 4, 3, 20, 15]"""
import sys,time
sys.stdin=open('in.txt','r')
sys.stdout=open('out.txt','w')
start_time = time.time()
class solution:
    def kthsmallest(self,arr,k):
        arr.sort()
        print(arr[k-1])
obj = solution()
arr = [7, 10, 4, 3, 20, 15]
k = 1
obj.kthsmallest(arr,k)
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()