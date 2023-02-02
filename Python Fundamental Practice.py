import random
import math

#1
def centralten(x, y, z):
    #mean
    mean = (x + y + z)/3

    #median
    if x < y:
        if y < z:
            median = y
        else:
            if x < z:
                median = z
            else:
                median = x
    else:
        if x < z:
            median = x
        else:
            if y < z:
                median = z
            else:
                median = y
    return mean, median
#2
def rand0m():
    a = random.randint(1,100)
    print(a)
    if (a%2==0 or a%3==0 or a%5==0):
        return True
    else:
        return False
#3
def lists(a,b,c,d,e,f,g,h,i,j):
    L=[a,b,c,d,e,f,g,h,i,j]
    Max=max(L)
    Min=min(L)
    Range=(int(Max) - int(Min))
    return Max, Min, Range
#4
def polarcoordinate(q,p):
    #distance
    p=[q,p]
    p0=[0, 0]
    Point = math.dist(p, p0)
    #angle
    tan= (p[0]/p[1])
    a = math.atan(tan)
    angle = math.degrees(a)
    return Point, angle

#5

    

def main():
        print(centralten(3, 5, 6))
        print(rand0m())
        print(lists(1,2,3,4,5,6,7,8,9,12))
        print(polarcoordinate(4,4))





if __name__=="__main__":
    main()

        
        
