import pystart
pystart.main()
"""Given an array, rotate the array by one position in clock-wise direction."""
class solution:
    def rotate(self,a,n):
        arr1=[]
        arr1.append(a[n-1])
        arr1=arr1+a[0:n-1]
        return arr1
    def display(self):
        a=[]
        n = int(input("Enter number of elements : "))
        for i in range(0,n,+1):
           a.append(int(input("Enter element :")))
        print(self.rotate(a,n))

obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()    