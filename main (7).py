'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.

'''

n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count==2 or n==2):
    print('Prime')
else:
    print('Not Prime')
