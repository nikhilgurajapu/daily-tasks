#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorilal_of_num(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    print(res)



n= 5
factorilal_of_num(n)

#factorial Of 5 = 5*4*3*2*1