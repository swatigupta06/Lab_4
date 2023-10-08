#Ques10
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
D = (b**2)-4*a*c

if D>0:
    x1 = (-b + (D)**(0.5))/(2*a)
    x2 = (-b - (D)**(0.5))/(2*a)
    print(x1, x2)
elif D==0:
    x1 = -b/(2*a)
    x1 = x2
    print(x1,x2)
elif D<0:
    i = (-1)**(0.5)
    D = D*i
    x1 = (-b + (D)**(0.5))/(2*a)
    x2 = (-b - (D)**(0.5))/(2*a)
    print(x1,x2)