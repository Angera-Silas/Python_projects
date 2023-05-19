def area(l,w):
    return lambda a:l*w
rect1=area(2)
print(rect1(20,30))