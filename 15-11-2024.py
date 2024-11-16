

#practicing the old topics and theory


#sorted:-returns a new sorted list.the original list is not sorted.

list2=[5,9,4,6,1,2]
list3=sorted(list2)
print(list3)

#Write a program that forms a list of first character of every word in another list.
list_1=["hellow","wellcome","to","the","world","of","python"]
letters=[]
for word in list_1:
    letters.append(word[0])
print(letters)




#Write a program to create a list of numbers on the range 1 to 10 , then delete all odd numbers from the list and print the final list.
list_num=[]
for i in range(1,11):
    list_num.append(i)
print("original list: ", list_num)
for index, i in enumerate(list_num):
    if (i%2!=2):
        del list_num[index]
print("list after deletiong odd numbers: ", list_num)


#write a program to create a list of numbers in the specied range in particular steps.Reverse the list and print its values.
num_list=[]
m=int(input("Enter the starting of the range: "))
n=int(input("Enter the ending of the range: "))
o=int(input("Enter the step in the range: "))
for i in range(m,n,o):
    num_list.append(i)
print("Original list: ", num_list)
list_num.reverse()
print("Reversed list: ", num_list)



#Write a program to determine whether a person is eligible to vote or not . if he is not eligoble , display how many yers left to be eligible.
age=int(input("Enterthe age: "))
if(age>=18):
    print("your eligible to vote: ")
else:
    yers=18-age
    print("your have to wait for another" +" "+str(yers) + "yesrs to cast your vote")


#Write a program that prints the multiplication table for a given number.
n=int(input("Enter the value: "))
print("multiplication table of: ",n)
for i in range(1,11):
    print(n,'x',i,'=',n*i)


#write a program to check if a number is an Armstrong number
n =int(input("enter a number:"))
temp=n
1==len(str(n))
sum=0
while(temp):
    r=temp%10
    sum=sum+r**1
    temp=temp//10
    print(sum)
if(sum==n):
    print("is a armstrong Number")
else:
    print("is not an Armstrong number")

#Python program to replace the string space with a given character. 
s="python"
c= "open source program"
s1=" "
for i in s:
    if i==" ":
        s1+=c
    else:
        s1 += i
print("string: ",s1)


#Python program to remove blank space from string. 
ss1=input("Enter a string: ")
print(len(ss1))
ss2=(ss1.strip())
print(len(ss2))
print(ss2)


#Python program to count alphabets, digits and special characters. 
str13=input("Enter a string: ")
alphabets=0
digits=0
specialc=0
for ch in str13:
    if ch.isalpha():
        alphabets=alphabets+1
    elif ch.isdigit():
        digits=digits+1
    else:
        specialc=specialc+1
print("alphabets count: ",alphabets)
print("digits count: ",digits)
print("special chara count: ",specialc)


"""reduce"""
from functools import * 
l = [1,2,3,4,5,6,7,8,9]
rs = reduce(lambda x,y : x+y,l)
print(rs)