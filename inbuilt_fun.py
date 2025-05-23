a="@ Python Is A Interpreter Language Version 3.13"
u=0
l=0
n=0
s=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        n+=1
    else:
        s+=1
print("upper charcter:",u)
print("lower charcter:",l)
print("numbers:",n)
print("special charcter:",s)



