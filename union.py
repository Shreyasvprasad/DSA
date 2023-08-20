import pystart
pystart.main()
"""Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays."""
class solution:
   def union(self,a,b):
      c=[]
      for i in a:
            c.append(i)
      for i in a:
            if i not in c:
               c.append(i)     
      return len(c),c      
   def display(self):
      a=[]
      b=[]
      n = int(input("Enter number of elements : "))
      for i in range(0,n,+1):
         a.append(int(input("Enter element : ")))
      m = int(input("Enter number of elements : "))
      for i in range(0,m,+1):
         b.append(int(input("Enter element : ")))
      print(self.union(a,b))

         
obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()