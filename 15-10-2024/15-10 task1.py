#Find Maximum: Write a program that finds the maximum number in a list .
number = [1,2,34,5,678,45,67,34,54]
num_len = len(number)
output = []
for i in range(num_len):
    output.append(i)
    if i not in output and i>output[0]:
        output.insert(output(0),i)
        print(output)

print(max(number))


"""def max_value_of_nums(number):
    max_value = number[0]
    for num in number:
        if num >max_value:
            max_value = num
            return max_value

number = [1,2,34,5,678,45,67,34,54]
output = max_value_of_nums(number)
print(output)"""