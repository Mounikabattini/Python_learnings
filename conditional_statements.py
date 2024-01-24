1)https://www.codesdope.com/course/python-print/
2)https://www.w3resource.com/python-exercises/python-basic-exercises.php
3)https://www.programiz.com/python-programming/methods/string/rsplit
4)https://www.sanfoundry.com/python-problems-solutions/#python-basic-programs
5)Telusko youtube channel



NOTES:
------
FUNCTIONS ------https://pynative.com/python-functions/


name=input("Enter the name:")
if name=="Durga":
	print("Hello durga ")
	print("how are you")
print("welcome to python")

2)AGE TO VOTE

age=int(input("Enter the age:"))
if age>=18:
	print("eligible to vote")
else:
	print("not eligible to vote")

3) EVEN OR ODD
num=int(input("Enter the number"))
if num%2==0:
	print("the number is even")
else:
	print("the number is odd")

4)DIVISIBLE BY 7?

num=int(input("Enter the number:"))
if num%7==0:
	print("the number is divisible")
else:
	print("the number is not divisible")

5)

num=int(input("enter the number:"))
if num%5==0:
	print("Hello")
else:
	print("Bye")

6)PRINT LAST DIGIT

num=int(input("enter the number:"))
print("Last digit number",num%10)

7)

more=True
while more == True:
	'''taking information from student'''
	name=input("enter stud name:")
	math_marks=int(input("enter math marks:"))
	eng_marks=int(input("enter eng marks:"))
	science_marks=int(input("enter science marks:"))
	social_marks=int(input("enter social marks:"))
	total=math_marks + eng_marks + science_marks + social_marks
	percentage=(total/400)*100
	print(name,"your marks are",total, "and your percentage is",percentage)
	
	a = input("enter another time y/n:")
	if a!="y":
		more=False

8)

name=""
pwd=""
while (name!="mouni") or (pwd!="raj"):
	name=input("enter your name:")
	pwd=input("enter your password:")
print("thanks for conforming")

9)

s="a9e3y4u6"
output = ''
for x in s:
	if x.isalpha():
		output=output+x
		previous=x
	else:
		output=output+previous*(int(x)-1)
print(output)


10)MATRIX FORM:
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
for r in x:
	print(r)
print("elements in matrix form:")
for i in range(len(x)):
	for j in range(len(x[i])):
		print(x[i][j],end=' ')
	print()
	

    
