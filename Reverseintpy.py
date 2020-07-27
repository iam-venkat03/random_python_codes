class Solution(object):
    def reverse(self,x):
        if x > 0:    
            a =  int(str(x)[::-1])  
        if x <=0:  
            a = -1 * (int(str(x*-1)[::-1]))  
        return a
d=Solution()
a=int(input())
print(d.reverse(a))

