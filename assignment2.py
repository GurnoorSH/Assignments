#Gurnoor Singh 21103010 CSE
#ASSIGNMENT 2

#Question 1
string= "Python is a case sensitive language"
#part a
print('Length:',len(string))
#part b
r=string[-1::-1]
print(r)
#part c
s=string[10:26]
print(s)
#part d
re=string.replace("a case sensitive", "object oriented")
print(re)
#part e
i=string.find("a")
print(i)
#part f
ws=string.replace(" ", "")
print(ws)

#Question 2
name=input("Please enter your name: ")
sid=input("Enter SID: ")
dep=input("Enter department name: ")
cgpa=float(input("Enter CGPA: "))
print('''Hey, %s Here!
         My SID is %s 
         I am from %s department and my CGPA is %s'''%(name,sid,dep,cgpa))
         
#Question 3
a=56
b=10
#part a
c=a&b
print("Part a:", c)
#part b 
d=a|b
print("Part b:",  d)
#part c
e=a^b
print("Part c:", e)
#part d
x=a<<2
print("Part d, (a):", x)
y=b<<2
print("Part d, (b):", y)
#part e
p=a>>2
print("Part e, (a):", p)
q=b>>4
print("Part e, (b):", q)

#Question 4
l=[]
for i in range(3):
        num=float(input("Enter number %s: "%(i+1)))
        l.append(num)

l.sort(reverse=True)
print("The greatest number is:",l[0])
 
#Question 5
str=input("Enter a string : \n")
namecount=str.count("name")
if 'name' in str:
        print("yes")
else:
        print("no") 
    

#Question 6
a=int(input("Enter first side="))
b=int(input("Enter second side="))
c=int(input("Enter third side="))
if c>=a+b :
 print("NO")
elif b>=a+c :
 print("NO")
elif a>=b+c :
 print("NO")
else :
 print("YES")
