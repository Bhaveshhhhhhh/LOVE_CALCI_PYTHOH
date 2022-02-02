# LEAP YEAR CALCULATOR
# y = int(input("enter the year:\n"))
# if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
#      print("Leap year")
# else:
#     print("normal year")        

print("WELCOME TO THE LOVE CALCULATOR")
name = input("Enter your name:\n") 
crush_name = input("Enter your crush name:\n")
string = name + crush_name
n1 = string.lower()
t = n1.count("t")
r = n1.count("r")
u = n1.count("u")
e = n1.count("e")
l = n1.count("l")
o = n1.count("o")
v = n1.count("v")
x = t + r + u + e 
y = l + o + v + e  
print(f"Your love percent is {x}{y}%")
if x > y :
        print("true love")
elif x < y :
        print("true hate")
else:
        print("no love")        