#lambda and filter function
nums = [1,2,3,4,5,6,7,8,9,10]
even_num = filter((lambda x : x % 2 == 0),nums)
print(list((even_num)))

print("----------------------------------------------------------")

odd_num = filter((lambda x : x % 2 != 0),nums)
print(list((odd_num)))