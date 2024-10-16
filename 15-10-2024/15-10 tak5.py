#10. Filter Even Numbers: Write a program that filters out all even numbers from a list and returns a new list of only odd numbers.
def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)
    return numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
result = filter_even(numbers)
print(result)