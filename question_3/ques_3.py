import json
from itertools import combinations as cb


x_cord = []
y_cord = []
combi = []



def combination(l):
    total_cb = cb(l,4)
    return total_cb
    

def distSq(p, q):
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

def isquare(p1,p2,p3,p4):
    
    d2 = distSq(p1, p2)
    d3 = distSq(p1, p3)
    d4 = distSq(p1, p4)
    
    if d2 == 0 or d3 == 0 or d4 == 0:
        return False
    
    if d2 == d3 and 2 * d2 == d4 and 2 * distSq(p2, p4) == distSq(p2, p3):
        return True

    if d3 == d4 and 2 * d3 == d2 and 2 * distSq(p3, p2) == distSq(p3, p4):
        return True

    if d2 == d4 and 2 * d2 == d3 and 2 * distSq(p2, p3) == distSq(p2, p4):
        return True

    
    
    
n = 1
while (n!=0):
    x = int(input())
    y = int(input())
    
    x_cord.append(x)
    y_cord.append(y)
    
    combi.append([x, y])
    
    print(combi)

    d = { "x": x, "y": y}

    a = json.dumps(d)

    dict = {"status" : "success"}

    print(a)
    print("Output:")
    print(json.dumps(dict))
    j = combination(combi)
    for i in j:
        if isquare(i[0],i[1],i[2],i[3]):
            print("Yes",i)
            
    
    

