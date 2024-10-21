#python program to check it is digit or not
def is_digit(integer):
    for i in integer:
        if i.isdigit():
            print("yes it is a digit")

integer = "1"
is_digit(integer)
