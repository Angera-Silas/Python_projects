def area(w):
    return lambda l:l*w
rect1=area(20)# This goes to w at the 
print(rect1(30))