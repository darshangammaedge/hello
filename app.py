# print("Darshan Patidar")
# print('o----')
# print(' ||||')
# print('*' * 10)


# # take input in python
# # name = input("enter your name: ")

# # dynamic printing or variable using f
# # print(f"hello {name} Welcome")

# # taking multiple inputes
# # x,y = input("inter 3 numbers : ").split()
# # print(f"1st : {x} 2nd : {y}")
# s = "1 22 33 44 55"
# word = s.split()  # split string using space or you can pass any parameter to split string as .split("',')
# print( s.split())
# print(word)


# # Swap two variables without temp variable
# a ,b = 2 , 3
# print(a,b)
# a ,b = b ,a
# print(a,b)

# # find length of string
# word = "python"
# length = len(word)
# print(length)


# # operators
# a =5
# b =10
# print("Addition : ", a+b )
# print("substration : ", a-b)
# print("Multiplications : " , a*b)
# print("Division : " , a/b)
# print("Floor division : " , a // b)
# print("modulus : " , a%b)
# print("exponentiation : ", a**b)

# # logical operator
# a = True
# b =False
# print(a and b)
# print(a or b)
# print(not a)

# #identity operators (is , is not)
# a =10
# b = 20
# c =a
# print(a is not b)
# print(a is c)

# # Membership operator ( in , nor in)
# x = 24
# y = 20
# list =[10, 20, 30, 40 ,50]
# if(x not in list):
#     print("x is not present in given list")

# else:
#     print("x is present in given list")

# if(y in list):
#     print("y is present in list")
# else:
#     print('y is not present in list')            


# #Ternary Operator (It simply allows testing a condition in a single line replacing the multiline if-else)

# a,b = 10 , 20

# min = a if a < b else b
# print(min)


# # operator preference
# expr = 10 + 20 * 30
# print(expr)
# name = "Alex"
# age = 0

# if (name == "Alex" or name == "John" and age >= 2):
#     print("Hello! Welcome.")
# else:
#     print("Good Bye")



# # match case ( switch case)

# number = 10

# match number:
#     case 1:
#         print("one")
#     case 2 | 3:
#         print("two or three") 
#     case 10:
#         print("ten") 
#     case _:
#         print("other number")    



# # making calculator using match

# # a , b = map(int,input("enter 2 numbers : ").split())
# # print(a,b)
# # ch = input("enter operator : ")

# # match ch:
# #     case '+': print("Addition : ", a+b)
# #     case '-': print("substraction : ", a-b)
# #     case '/': print("division : ", a/b)
# #     case _: print("enter valid operator")



# # Loops 
# # for loop
n =4 
for i in range(0,n):
    print(i)    


