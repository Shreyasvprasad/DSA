import pystart
pystart.main()
"""Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the intersection between these two arrays."""
class solution:
   def inter(self,a,b):
      c=[]
      for i in a:
         if i in b:
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
      print(self.inter(a,b))

         
obj = solution()
obj.display()
print("-----%s seconds-----"%(time.time()-start_time))
sys.stdin.close()
sys.stdout.close()