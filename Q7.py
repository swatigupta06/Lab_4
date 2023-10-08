#Ques7
a = 1
b = int(input("enter the second term of sequence: "))
c = int(input("enter the third term of sequence: "))
d = int(input("enter the fourth term of sequence: "))
e = int(input("enter the fifth term of sequence: "))
f = int(input("enter the sixth term of sequence: "))
print("given sequence", a,b,c,d,e,f)
if a==b and a+b==c and b+c==d and c+d==e and d+e==f:
    print("sequence is fibonacci")
else:
    print("sequence isn't fibonacci")
