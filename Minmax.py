"""Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array."""
import sys,time
sys.stdin=open('in.txt','r')
sys.stdout=open('out.txt','w')
start_time = time.time()
class solution:

    def minmax(self,a):
        min=max=a[0]
        for i in a :
            if i<min :
                min=i
            elif i>max:
                max=i
        return max,min 

    def display(self):
       a=[]
       n = int(input("Enter number of elements : "))
       for i in range(0,n-1,+1):
           a.append(int(input("Enter element : ")))
       print(self.minmax(a))
         
obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()
