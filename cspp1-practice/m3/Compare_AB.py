m=input("Enter the value of a")
n=input("Enter the value of b")

try:
    VarA =int(a)
    VarB =int(b)
    if VarA< VarB:
        print("smaller")
    elif VarA == VarB:
        print("equal")
    else:
        print("bigger")

except:
    print("string involved")
    
    
    
    
    
