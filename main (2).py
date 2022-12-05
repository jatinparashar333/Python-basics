Find the Sum of the First N Natural Numbers in Python
Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer.


'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
num=int(input())
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)