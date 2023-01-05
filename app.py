"""
def addnums(x,y):
    z=x+y
    return z
print(addnums(989898,100000000))
def evenorodd(n):
    if(n%2==0):
        return("even")
    else:
        return("odd")
print(evenorodd(48))

def greatest(*a):
    print(max(a))

greatest(1,5,7,8,9,67,68,98,45)"""
def prieven(*a):
    x = []
    y=[]
    for n in a:
      if(n%2==0):
        x.append(n)
      else:
          y.append(n)
    print(x)
    print(y)
    x.sort()
    x.reverse()
    y.sort()
    y.reverse()
    print(x)
    print(y)
prieven(1,41,63,66,88,23,56,78,89,35,57,77,20,23,34,12,21,33)


