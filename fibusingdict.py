def fib(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib(n-1,d) + fib(n-2,d)
        d[n]=ans
        return ans
d={0:1,1:1,2:1,3:2}
number = int(input())
print(fib(number,d))
