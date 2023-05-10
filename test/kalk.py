import math 

def cube_m(a,b,c,p):
    return a*b*c*p/1000


def tube_m(D,d,h,p):
    v1=math.pi*((D*2)^2)*h
    v2=math.pi*((d*2)^2)*h
    m=(v1-v2)/1000*p
    return m 

def mass(m,n,k,f):
    k1=n*k*f/42.02
    m1=(m *(k1/100))/(1+(k1/100))
    m2=m-m1
    return m1,m2

def mass_ot(m,n,k,f):
    k1=n*k*f/42.02
    m1=((k1/100)/(1+k1/100))*m/(1-(k1/100)/(1+k1/100))
    return int (m1+(0.5 if num > 0 else -0.5))