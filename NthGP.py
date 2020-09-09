def findNthGP(input1, input2, n):
    r = input2/input1
    a1 = input1/r
    return round(a1*(r**(n-1)),3)

if __name__=="__main__":
    print(findNthGP(float(1),float(2),int(4)))
    print(findNthGP(float(-4),float(-8),int(5)))
    print(findNthGP(float(-8),float(4),int(6)))