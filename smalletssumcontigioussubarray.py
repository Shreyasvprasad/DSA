import pystart
pystart.main()
""" Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the minimum sum and return its sum."""
class solution:
    def minsum(self,a):
        minsofar=a[0]
        minendinghere=0
        for i in range(0,len(a),+1):
                minendinghere=0
                for j in range (i,len(a),+1):
                    minendinghere+=a[j]
                    if (minsofar>minendinghere):
                        minsofar=minendinghere
        return minsofar                
    def display(self):
        a=[-2,-6,8,1,4]
        print(self.minsum(a))
obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()