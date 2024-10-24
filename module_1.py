def mul(x,y):
    return x*y

def add(x,y):
   return x+y

def even_nums(x):
    evens = []
    for i in x:
        if i % 2 == 0:
            evens.append(i)
    return evens