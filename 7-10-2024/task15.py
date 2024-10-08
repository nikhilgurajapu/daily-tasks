"""Python program to print all non repeating character in string"""
input = "re-unionisorganising"
for i in input:
    count = 0
    for j in input:
        if i == j:
            count += 1
        if count > 1:
            break
if count == 1:
    print(i, end="")
     