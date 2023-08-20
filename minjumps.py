import pystart
pystart.main()
""" Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the minimum sum and return its sum."""
class solution:
    def minjumps(self,arr,n):
        if n == 1:
            return 0
        res = float('inf')
        for i in range(n-1):
            if (i + arr[i] >= n-1):
                sub_res = minJumps(arr, i+1)
                if sub_res != float('inf'):
                    res = min(res, sub_res + 1)
        return res

obj = solution()
obj.minjumps(arr,)
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()