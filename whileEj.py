"""
x = 6
while x > 1:
    x -=1
    print(x)
"""
"""
x=int(input("cuantos son: "))
while x>0:
    c=int(input("que edad tienes: "))
    if c < 18:
        print("eres menor de edad no puedes pasar")
        break
    else:
        x-=1; 
"""
x=1;
j=1;
c=1
while x < 10:
    frace=f"------TABLA DE {x} -------"
    print(frace)
    while j < 11:
        print(x,"X", j, "=", (j * x))
        j+=1
    j=c
    x+=1
