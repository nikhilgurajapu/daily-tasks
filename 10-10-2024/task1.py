input_data = [[1,2,3],[4,5,6],[7,8,9]]
"""
output
123
456
789
"""
"""l = []
input_len = len(input)
for i in range(input_len):
    for j in input:
        l.append(input[0:1])
print(l)"""

for row in input_data:
    ''.join(map(str,row))
    print(str(row))

    
