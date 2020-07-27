def pal(s):
    s=s.lower()
    s=''.join(s.split())
    if len(s)==1 or len(s)==0:
        return True
    else:
        return s[0]==s[-1] and pal(s[1:-1])
m=str(input("Enter the string"))
print(pal(m))
