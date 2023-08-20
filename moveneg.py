"""Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element"""
import sys,time
sys.stdin=open('in.txt','r')
sys.stdout=open('out.txt','w')
start_time = time.time()
class solution:
    def movenegtoend(self,arr,n):
        arr1=[]
        arr2=[]
        for i in range(0,n,+1):
            if arr[i]<0:
                arr1.append(arr[i])
            else:
                arr2.append(arr[i])
        arr2=arr2+arr1
        return arr2        
    def display(self):
        arr=[]
        n = int(input("Enter number of elements : "))
        for i in range(0,n,+1):
           arr.append(int(input("Enter element : ")))
        print(self.movenegtoend(arr,n))

obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()