#21103010 CSE Gurnoor Singh 
#Q1
a=input("Enter first number: ")
b=input("Enter second number: ")
c=input("Enter third number: ")
d=(int(a)+int(b)+int(c))/3
print("The average of three numbers is :",d)

#Q2
standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income: ")
No_of_dependents=input("Enter your number of dependents: ")
taxable_income=int(gross)-(standard_deduction)-((depend_deduction)*int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :",tax)

# Question 3
SID=input("Enter your SID:")
Name=input("Enter your name:")
Gender=input("Enter your Gender: ")
Course_name=input("Enter your course name:")
CGPA=float(input("Enter your CGPA:"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)


# Question 4
mlist=[]
for i in range (5):
        mlist.append(float(input("Enter marks of Student:") ))                            
mlist.sort()
print(mlist)

# Question 5
color=['Red','Green','White','Black','Pink','Yellow']
color.remove(color[3])
print("Part (a) of question : ",color)
color[3:5]=['Purple']
print("Part (b) of question :",color)

