#!/usr/bin/env python
with open('6input', 'r') as f:
    lines = f.read().splitlines()
print(lines)

input_string = lines[0]
for i in range(14,len(input_string)):
    if len(''.join(set(input_string[i - 14:i]))) == 14:
        print(i, input_string[i - 14:i])
        break
