#3. Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

def mul_nums_in_list(sl):
    mul = 1
    for i in sl:
        mul = mul*i
    return mul
        

sl = [8, 2, 3, -1, 7]
print(mul_nums_in_list(sl))