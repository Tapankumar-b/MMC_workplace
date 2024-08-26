"""
Q-1.Whatis decorator , write a decorator?
Ans:-
Decorator: if you want to execute another function logic into your code as an argument then we are using decorator.
Using yield keyword we are calling one funtion.
It returns a new function that adds functionality to the original function.
Example:-
def add_num(x, y):
    return x + y
result = add_num(3, 5)
print("display the result:-" result )

Q-2.What is lambda expression and write lambda expression code?
Ans:-
if you want to express your ligic in a single line then we can use lambda expression. 
it will reduce the line of code
Ex:-
a = lambda x: x + 10
result = a(5)
print(result)

Q-11.Difference between List vs tuple vs set vs dictionary?
Ans:-
List ***
It contains heterogenious data
list syntax is []
duplicated are allowed
its mutable
it is less faster than list
list = [1, 2, 3, 4]

Tuple:-
It contains heterogenious data
Tuple syntax is ()
duplicated are allowed
its immutable
its faster than List
tuple=(1,2,3)

Set:-
Set syntax is {}
duplicated are not allowed
its mutable
set={1,2,3}

Dictionary[]:-
It contains Key and value pair
Dictionary syntax is [Key: keyname,value: Value name]
value can be duplicate but Key always unique
dic=['a':1,'b':2]

12.What is Garbage Collection?
Ans:-
it is nothing but it will delete the assigined value if we mordify the existing value with new value

Q-10 Difference between Moudle and Packages (3 diff)
Ans:
-Module it used for a single python file 
-module can be class,variable etc.
-package it is a combination of multiple pythone file.
-when we create package by default -init.py will create

Q-4:  WAF,Reverse a string words.
 > Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function
Ans:
Input = "hello world"
output=""
for i in Input:
    output=i+output
print(output)

Q-5: WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’
Ans:-

Q-8: Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
 the csv and print in console bar
import  csv
data1=["first_name" , "email", "phn_no"]
data2=[["Tapan","tapankumarbehera1522@mail.com",9583156237],["abc","abc@mail.com",1234567890],["abc","abc@mail.com",12345678980],["abc","abc@mail.com",1234567890]]
with open("result.csv",mode="w") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(data1)
    csv_writer.writerows(data2)
with open("result.csv",mode="r") as file:
    csv_reader=csv.reader(file)
    for i in csv_reader:
        print(i)


Q-9:- Whatis exception handling , how handel the exception in python , explain with each
 block
Ans:-
Exception handling means to handele the abnormal tarmination of an program.
we can handle exception handling using try,except and finally.
in try block we can rise the exception
in except block we can handle the exception
Finally block will execute at last it will execute compusury if we declare finally.

Q-15:  Explain break, continue, pass with code?
Ans:-
Break will stope the itteration
continue will start the itteration


"""