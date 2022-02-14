#QUESTION1

a=str(input("ENTER A STRING: "))
list=a.split() 
dict={} 
if list.__len__()==1: 
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                 
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")

#QUESTION2


def Next_Date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):                 #while loop is used so that if any wrong value is entered  then values will be entered again
        day=int(input("ENTER THE DAY: "))
        if(1<=day<=31):
            break
        else:
            print("Please Enter a valid day")
    while(True):                  #while loop is used so that if any wrong value is entered  then values will be entered again
        month=int(input("ENTER THE MONTH OF THE YEAR: "))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    while(True):                #while loop is used so that if any wrong value is entered  then values will be entered again
        year=int(input("ENTER THE YEAR: "))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print(day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN") 
            Next_Date()      
    elif month in list3:
        if(year % 4 == 0):  
            if(day==29):
                day=1
                month=month+1
                print(day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1;
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
        
    else:
        print("INVALID DATE TRY AGAIN")
        Next_Date()
Next_Date()
print("\n")

#QUESTION3

inputlist = input('Enter elements separated by space: ')
user_list = inputlist.split()

print('list: ', inputlist)


for i in range(len(user_list)):

    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(squarelist)

print("\n")

#QUESTION4

grade=int(input("Give a number between 4 and 10: "))


if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


#QUESTION5

Word="ABCDEFGHIJK"

i=1

while(i<7):
    print(" "*(i-1),Word[0:11-((i-1)*2)])
    i=i+1

    
#QUESTION6

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("<a>",students)

#part b. sort acc to the names
print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c>",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("<d>",students[sid])    

#QUESTION7


print("QUESTION 7")
#  Function to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("AVERAGE IS:",avg)


#QUESTION 8

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
print("(a)")
required_Set=Set1^Set2
print(required_Set)


#(b)
print("(b)")
required_Set=Set1^(Set2^Set3)
print(required_Set)


#(c)
print("(c)")
required_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(required_Set)


#(d)
print("(d)")
new_Set={1,2,3,4,5,6,7,8,9,10}
required_Set=new_Set-Set1
print(required_Set)


#(e)
print("(e)")
required_Set=new_Set-(Set1|Set2|Set3)
print(required_Set)
