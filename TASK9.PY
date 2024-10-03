"""a program that generates a random number between 1 and 100, and asks the user to guess it. The program should give hints ("too high" or "too low") until the user guesses correctly."""
n = int(input('enter input:'))
if n >60:
    print("your guess is high")
elif n>=80:
    print("your guess is too high")
elif n<60:
    print("your guess is low")
elif n<=30:
    print("your guess is too low")
elif n==60:
    print("Great you guess a correct number")
