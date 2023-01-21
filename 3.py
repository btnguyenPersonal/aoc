#!/usr/bin/env python
priorities = ''
with open('3input', 'r') as f:
    lines = f.readlines()
for i in range(0, len(lines), 3):
    priorities += (''.join(set(lines[i].strip()) & set(lines[i+1].strip()) & set(lines[i+2].strip())))
    print(priorities)
sum = 0
for i in range(len(priorities)):
    if priorities[i].isupper():
        sum += ord(priorities[i]) - 65 + 27
    if priorities[i].islower():
        sum += ord(priorities[i]) - 96
print(sum)