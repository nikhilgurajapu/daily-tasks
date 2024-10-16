#7. Merge Two Lists: Create two lists and write a program to merge them into a single list, ensuring there are no duplicates.
l1 = ["eleven","ten","two","four","five"]
l1_len = len(l1)
l2 = ["nine","two","eight","five","ten"]
l2_len = len(l2)
for i in l1_len:
    if l1[i] in l2:
        l2.remove(l1[i])
    print(l2)

print(l1 + l2)


