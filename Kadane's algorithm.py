import pystart
pystart.main()
"""Kadane's algorithm: Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum."""
class solution:
    def maxsum(self,a):
        maxsofar=a[0]
        maxendinghere=0
        for i in range(0,len(a),+1):
                maxendinghere+=a[i]
                if (maxsofar<maxendinghere):
                    maxsofar=maxendinghere
                elif(maxendinghere<0):
                    maxendinghere=0
        return maxsofar                
    def display(self):
        a=[-2,-3,4,-1,-2,1,5,-3]
        print(self.maxsum(a))



obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()