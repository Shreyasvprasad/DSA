
"""Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order."""
class Solution:
   def sort012(self,arr,n):
        one=0;
        zero=0;
        two=0;
        for i in range (0,n,+1):
            if arr[i]==0:
                zero+=1
            elif arr[i]==1:
              one+=1
            else:
              two+=1
        for i in range (0,zero,+1):
            arr[i]=0   
        for i in range (zero,zero+one,+1):
            arr[i]=1
        for i in range (zero+one,zero+one+two,+1):
            arr[i]=2
            
        print(arr)    
obj = Solution()
obj.sort012([1,0,1,2,2,1,2,0,2,0,0,2,1,0,0,1,1],17)