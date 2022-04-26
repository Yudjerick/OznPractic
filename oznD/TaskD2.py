import math

def A(x,y,d):
    return d*((x**2-1)/(math.fabs(3.25*y)+1))**(1/3)+ math.tan(3*x)**2 - 0.1

def B(x,y,c,a):
    return math.sin(x)**2 + 0.55*(pow(math.e, x*y) + 1) - (4*x - 6.25*c)/(a*c*y)

print(A(3,1,1))
print(B(2,2,2,2))
