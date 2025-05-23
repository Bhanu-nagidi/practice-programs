def string1(a):
    num=0
    for i in a:
        if i.isdigit():
            num+=1
        
    return num

a=input("enter:")
print(string1(a))
