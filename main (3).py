Find the Sum of the Numbers in a Given Interval in Python Language
Given two integer inputs as the range [low , high], the objective is to 
find the sum of all the numbers that lay in the given integer inputs as interval.
In order to do so we usually iterate through 
the numbers in the given range and keep appending them to the sum variable



'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
num1=int(input())
num2=int(input())
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print(sum)