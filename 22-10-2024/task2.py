#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_of_nums_in_list(sl):
    return sum(sl)

sl = (8, 2, 3, 0, 7)
print(sum_of_nums_in_list(sl))