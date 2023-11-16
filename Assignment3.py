#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""IF Statement
Problems:
1. Write a program to check whether x is less than y
where, x = 20 and y = 30
Assigning x equal to 20 Assigning y equal to 30 If condition x is less then y then go to step 4 print x
is less then y"""
x=20
y=30
if x<y:
    print("x is less than y.")
if x>y:
    print("x is greater than y.")


# In[2]:


"""
2. Write a program to check whether the total score (theory --> 100 + practical --> 100) is less
than or equal to 200. If it goes beyond 200, print an error or a warning message.
Hint:
Set, Theory equal to 140 Practical equal to 145 If condition for theory + practical is greater than 200
then, print invalid score
"""

Theory = 140
Practical = 145
if Theory+Practical>200:
    print("Invalid Score")


# In[3]:


""" 
If-else Statement
3. Write a python program to to check whether the student has passed the subject based on
string input yes/no
Hint:
Get an user input 'yes' / 'no' pass this to variable named 'Subject' Create a If condition, when the
Subject value is 'yes' then print 'Cleared the test', Else print 'Failed the test'.
"""
Subject = input().lower()
if Subject=="yes":
    print("Cleared the test.")
else:
    print("Failed the test.")


# In[4]:


"""
4. Write a program to get the password from user, check whether the password is 'great'.
Through a reply to the user accordingly.
Hint:
Get password from user, the input statement should be 'Enter the password: ' pass this to variable
named 'Password' If passwrod is 'great', print 'Password Accepted' else print 'Wrong Password'
"""
Password = input("Enter the password : ")
if Password=='great':
    print("Password Accepted")
else:
    print("Wrong Password")


# In[5]:


"""
Nested if Statement
1. Based on the users age, divide them in to three groups Group 1 : Age <=18 , Minors who are
not eligible to work Group 2 : 18<Age<60 , ELigible to work Group 3 : >=60, Too old to work
as per govt. regulations.
Write a program for the same
Hint:
Create variable Name age equal to input if condition for age is < 18 go to step 3 , else go to step 5
print Your Minor not Eligible to Work if condition for age >= 18 and age <= 60 go to step 5 , else go
to step 6 print Your Eligible to Work fill in your details and apply print Your too old to work as per the
Government rules Please Collect your pension
"""
age = int(input())
if age<=18:
    print("You are Minor so you are not eligible to work.")
if age>=18 and age<60:
    print("You are eligible to work; Fill in your details and apply.")
if age>=60:
    print("You are too old to work as per the government rules; Please collect your pension.")


# In[6]:


"""
While Loop
1. Take an integer as input from the user and print all the numbers from 0 to that number in
reverse order.
Example : if the input is 3, the output should be 3 2 1
Hint:
Create variable n using input value give the while loop condition i.e. n > 0 then decrement, n = n-1
print n
"""
n=int(input())
i=0
while n>0:
    i=i+1
    if i==1:
        print(n,end=" ")
    else:
        n=n-1
        print(n,end=" ")


# In[7]:


"""
2. Write a python code to find the squares of all the numbers based on an input.
Example : If the input is 10, the output should be 11 ,22 ,33...... 1010
Hint:
Create the variable i assigning to 1 Give the while loop condition for i <= 10 print i ** 2 increment i
loop will execute until i is less than or equal to 10
"""
j=int(input())
i=1
while i<=j:
    print(i,end="")
    if i==j:
        print(i)
    else:
        print(i,end=" ,")
    
    i+=1


# In[8]:


"""
For Loop
1. Write a pseudocode to print the multiplication table of a given number.
Example : if the user input is 3, the output should be like below :
3 X 1 = 3 3 X 2 = 6 ... 3 X 10 =30
Hint:
Get user input and store it in variable n. Give the For loop condition in the range between (1,11) In
print statement give the condition (n,'x',i,'=' ,n*i) This will print the multiplication tables of a given
number.
"""
n=int(input())
for i in range(1,11):
    y=n*i
    print(n,"X",i,"=",y, end=" ")


# In[9]:


"""
2. Write a python code to print squares of all numbers present in the list = [1, 22, 14, 64, 31,
120]
Hint:
Create a list named 'numbers' [1, 22, 14, 64, 31, 120] Create a variable name 'square' and assign 0
to it For loop condition for i in the list square equal to i * i
Print square    
"""
numbers = [1,22,14,64,31,120]
square = 0
for i in numbers:
    square=i*i
    print(square)


# In[10]:


"""
Additional Practice Programs
1. Write a python program that takes a list ['red','black','blue'] and prints each element in the list
using while loop
"""
j=['red','black','blue']
i=0
while i<=len(j)-1:
    print(j[i])
    i+=1


# In[11]:


"""
2.Write a same program as above using a For loop?
"""
j=['red','black','blue']
for i in j:
    print(i)


# In[12]:


"""
3. Write a Python Program to find the LCM of two numbers?
"""
def lcm(x,y): #this function for finding the greatest common divisor was made using the concept of Euclidian algorithm
    lx=x
    ly=y
    c=1
    i=0
    d=0
    r=1
    g=0
    l=0
    if x<y:
       while i==0 :
            c=0
            d=0
            while c<y or c==y:
                d=d+1
                c=x*d
            c=x*(d-1)    
            r=y-c
            if r==0:
                break
            y=x
            x=r
    elif y<x:
        while i==0 :
            c=0
            d=0
            while c<x or c==x:
                d=d+1
                c=y*d
            c=y*(d-1) 
            r=x-c
            if r==0:
                break
            x=y
            y=r
    if x<y:
        g=x #gcd when x<y
    if y<x:
        g=y #gcd when y<x
    if lx*ly<0:
        l=-(lx*ly)/g
    else:
        l=(lx*ly)/g
    
    return l 
            
    
    

inpt1=int(input("Enter the first Number:"))
inpt2=int(input("Enter the second Number:"))
print(lcm(inpt1,inpt2))



# In[13]:


"""
4. Python Program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.

"""
def Sum_of_a_Series(N):
    sumofseries=0
    for i in range(1,N+1):
        sumofseries+=(1/i)
    return sumofseries

inpt= int(input("Enter the number of elements that  you  want add in the series:"))
print(Sum_of_a_Series(inpt))


# In[15]:


"""
List Comprehensions
1. i. Write a Python program to get the squares of numbers present in the range of (1-10)
● output squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
import math 
l=[]
for i in range(0,11):
    l.append(pow(i,2))
print(l)


# In[16]:


"""
2. Convert a list of integers to a list of strings, using List comprehension.
"""
intlist=[0,1,2,8,9,4,3,5,6,7]
l=[str(x) for x in intlist]
print(l)


# In[17]:


"""
3. Create tuples from two lists using List Comprehensions
Hint: list1 =[0,1] list2 =['zero','one']
Output: [(0, 'zero'), (0, 'one'), (1, 'zero'), (1, 'one')]
"""
list1=[0,1]
list2=['zero','one']
list3=[(x,y) for x in list1 for y in list2]
print(list3)


# In[18]:


"""
4. Get Index of Each Element of List using enumerate in List Comprehension
"""
l=['Cat','Mat','Rat']
lst=[(index,lst1) for index,lst1 in enumerate(l)]
print(lst) 


# In[ ]:




