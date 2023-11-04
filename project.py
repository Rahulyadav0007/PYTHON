# """x=345
# a=x%10
# print(a)
# A=a*100
# b=x//10
# a=b%10
# print(a)
# A=A+(a*10)
# c=b//10
# a=c%10
# print(a)
# A=A+(a)
# print (A)"""
# import math
# n=int(input("Enter any number: "))
# temp=n
# A=0
# no_of_digit=int((math.log10(n)))
# print(no_of_digit)
# while (n>0):
#     r=n%10
#     A+=r*(10**(no_of_digit))
#     no_of_digit-=1
#     n=n//10
# print (int(A))
# A=int(A)
# if A==temp:
#     print("Number is palindrome.")
# else:
#     print("Number is not palindrome.")

# n=123
# n=str(n)
# z=n[::-1]
# print(z)

# Current date and time

# import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime)

# fibonacci series

# number=int(input("Enter any number : "))
# i=2
# m=0
# n=1
# while(i<=number):
#     print(n,end=",")
#     temp=n
#     n=m+n
#     m=temp
#     i+=1

# print(n,end=",")


# def swapList(newList):
#     size = len(newList)
#     temp=newList[0]
#     newList[0]= newList[size-1]
#     newList[size-1]=temp
#     return newList

# newList=[12,13,42,55,66]
# print(swapList(newList))


# number=int(input("Enter any integer number upto which you want to print fibonacci series: "))
# m=-1
# n=1
# i=0
# print("Fibonacci series of range number: " )
# while (i<=number):
#     temp=n
#     n=n+m
#     m=temp
#     i+=1
   
#     print(n,end=",")

# import datetime
# current_datetime=datetime.datetime.now()
# print(current_datetime)

# n1=int(input("Enter the first operator: "))
# operator=input("Enter the operand(+,-,*,/,%): ")
# n2=int(input("Enter the second operator: "))

# if operator=="+":
#     print(n1+n2)
# elif operator=="-":
#     print(n1-n2)
# elif operator=="*":
#     print(n1*n2)
# elif operator=="/":
#     print(n1/n2)
# elif operator=="%":
#     print(n1%n2)
# else:
#     print("Invalid operation")


# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# print(n1+n2)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# d=int(input("Enter forth number: "))
# e=int(input("Enter fifth number: "))
# f=int(input("Enter sixth number: "))
# print(list [a,b,c,d,e,f])

# question no 5
# list=[11,31,43,11,22,10,20.1,10]
# dict={}
# key value pair
# aceessing the elements of the list
#normaally
# for i in range(0,len(list)):
#     print(list[i])

# print("printineeg by other method")
# for i in list:
#     if i not in dict.keys():
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)

# string={"A":"Apple","B":"Ball","C":"Cat","D":"Dog","E":"Elephant","F":"Fish"}
# print(string)
# dict= string
# dict={}
# for i in range(0,len(dict)):
#     print(dict[i])
# for i in string:
#     if i  not in dict.key():
#         dict[i]=1
#     else:
#         dict[i]+=1
#         print(dict)



# def fun(n):
#     if(n>100):
#     return n-5
#     return fun(fun(n+11))
# print fun(45)



# import os 
# print("Hello world")


# poem= ('''Twinkle, twinkle little star
#        how i wonder what you are !
#        up above the world so high
#        like a diamond in the sky.''')
# print(poem)
    

# n=4
# i=0
# while i<=10:
#     print(n*i)
#     i+=1



# word="Hello"
# letterList=list(word)
# a=letterList[0]
# b=letterList[1]
# letterList[0]=letterList[-1]
# letterList[1]=letterList[-2]
# letterList[-1]=a
# letterList[-2]=b
# print(letterList)
# word=",".join(letterList)
# print(word)

# FACTORIAL OF ANY NUMBER
    
# n=5
# fact=1
# while n>1:
#     fact*=n
#     n-=1
# print(fact)
 

# list=[10,23,534,233,22,100]
# sum=0
# for i in list:
#      sum+=i
# print(sum)


# set1={1,2,3,4,5,6,7,8,9}
# set2={2,5,6,9,11,12,15,20}

# print("union: ", set1|set2)
# print("intersection: ", set1&set2)
# print("Difference: " , set1-set2)
# for i in range:


# from playsound import playsound
# playsound('"C:\\Users\\Rahul\\Downloads\\Shubh - Cheques (Official Music Video).mp3"\\play.mp3')


# import os
# print(os.listdir())

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# mul=a*b
# print(mul)




    

   










