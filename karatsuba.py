def karatsuba(x,y):
    if (x<10 and y <10):
        return x*y
    else :
        n=(max(len(str(x)),len(str(y))))//2
        x1=x//(10**n)
        x2=x%(10**n)
        y1=y//(10**n)
        y2=y%(10**n)
        x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
        x1y1=karatsuba(x1,y1)
        x2y2=karatsuba(x2,y2)
        x1y2_plus_x2y1=karatsuba(x1+x2,y1+y2)-(x1y1+x2y2)
        ans=x1y1*(10**(n*2))+(x1y2_plus_x2y1*(10**n))+x2y2 
        return ans 
x=input()
y=input()
x,y=int(x),int(y)
print(karatsuba(x,y))
        
