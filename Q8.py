#Ques8
i = int(input())
if i == 1:
    print("given number isn't prime")
elif i == 0:
    print("given number isn't prime nor composite")
elif i < 0:
    print("given number cannot be defined as prime or not")
elif i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 :
    print("given number is prime")
else:
    print("given number isn't prime")
