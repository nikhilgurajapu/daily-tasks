n = 2
is_prime = True
for i in range(2, n+1):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)