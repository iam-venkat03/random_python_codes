class Solution(object):
    def isHappy(self, n):
        total=sqr=0
        x=[]
        while sqr!=1:
            total=0
            while n>0:
                total+=(n%10)**2
                n=n//10
            if total==1:
                return "Happy Number"
            elif total in x:
                return "False"
            else:
                n=total
                x.append(n)
d=Solution()
num = int(input())
print(d.isHappy(num))
