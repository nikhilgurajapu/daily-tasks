""" program to check if a number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits"""
n= 153
ln = 0
while n > 0:
    digit = n % 10
    ln += digit**3
    n //= 10


if n == ln:
    print(n,"is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")