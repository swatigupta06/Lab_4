#Ques9
line = str(input("enter the line: "))
l = len(line)

large = small = specialch = digits = 0 
for i in range(l):
    if(line[i]>="A" and line[i]<="Z"):
        large += 1
    elif(line[i]>='a' and line[i]<='z'):
        small += 1
    elif(line[i]>='0' and line[i]<='9'):
        digits += 1
    else:
        specialch += 1
    i += 1 
    