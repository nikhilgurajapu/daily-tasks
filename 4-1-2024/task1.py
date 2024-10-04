full_sequence = "pqrstu"

sub_sequence = "prst" 

"""sub_seq_len = len(sub_sequence)
sub_seq_index = 0

for char in full_sequence:
    if char == sub_sequence[sub_seq_index]:
        sub_seq_index += 1
        if sub_seq_index == sub_seq_len:
            break

if sub_seq_index == sub_seq_len:
    print("YES")
else:
    print("NO")"""
ln = len(full_sequence)

full_sequnce_2 = full_sequence[0:ln:2]
if sub_sequence == full_sequnce_2:
    print("yes")
else:
    print("no")