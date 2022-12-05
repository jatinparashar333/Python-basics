Find the Greatest of the Two Numbers in Python Language
Given two integer inputs, the objective is to find the largest number among the two integer inputs.
In order to do so we usually use if-else statements to check which one’s greater. 


'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
num1=int(input())
num2=int(input())
if num1==num2:
    print('equal')
elif num1>num2:
    print(num1)
else:
    print(num2)