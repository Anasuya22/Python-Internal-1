# -*- coding: utf-8 -*-
"""Python_Internal_Assessment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y1VtTMQR60Te_XHTFOCUAy-iyF-3YP_K

Q-1
"""

length=int(input())
breadth=int(input())
print("Area of rectangle is : "+ str(length*breadth))

"""Q-2"""

weight=float(input("enter weight in kgs"))
height=float(input("enter height in m"))
BMI=weight/(height)**2
print(BMI)

"""Q-3"""

stud_names=["Anasuya","Yasoda","Anjali","Divya"]
Scores=[28,30,24,26]
d={}

for key in stud_names:
    for value in Scores:
        d[key] = value
        Scores.remove(value)
        break
print(d)

"""Q-4"""

age=int(input("enter age"))
if age >0 and age<18:
  print("Minor")
elif age>=18 and age<=60:
  print("Adult")
else:
  print("Senior")

"""Q-5"""

Even_list=[]
for i in range(1,51):
  if i%2==0:
    Even_list.append(i)
print(Even_list)

"""Q-6"""

password=str(input("enter password "))
crct_password='Anasuya@22'
while (1):
  if password==crct_password:
    print("You have entered crct password")
    break

  else:
    print("enter crct password")
    break

"""Q-7"""

def avg_list(a_list):
  print(sum(a_list)/len(a_list))

a_list=[1,2,3,4,5]
avg_list(a_list)

"""Q-8"""

word=list((input().lower()))
count=0
vowel=['a','e','i','o','u']
for i in word:
  if i in vowel:
    count=count+1
print(count)

"""Q-9"""

from datetime import date

today = date.today()
print(today)

"""Q-10"""

def addition(a,b):
  try:
    s=int(a)+int(b)
    print(s)
  except ValueError:
    print("a,b must be numeric values")
a=(input())
b=(input())
addition(a,b)

"""Q-11"""

a=(input())
try:
  print(int(a))

except ValueError:
  print("Invalid Input....Enter integer")

"""Q-12"""

def division(a,b):
  try:
    s=a/b
    print(s)
  except ZeroDivisionError:
    print("b must not be zero")
  else:
    print("Division completed")
a=int(input())
b=int(input())
division(a,b)

"""Q-13"""

file=open("/content/Python_file.txt",'w')
l="HELLO python"
file.write(l)
file.close()

"""Q-14"""

file=open("/content/Python_file.txt",'r')

file.read()
file.close()

"""Q-15"""

file=open("/content/Python_file.txt",'r')
vAR_line = input() #take input

file.readlines()
file.close()