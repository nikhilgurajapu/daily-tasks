#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
def reverse_a_string(ss):
    sl = ss[::-1]
    return sl

ss = "1234abcd"
print(reverse_a_string(ss))
