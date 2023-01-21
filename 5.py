#!/usr/bin/env python
with open('5input', 'r') as f:
    lines = f.read().splitlines()

def print_stack(stack):
    i = 1
    for col in stack:
        print(i, end=' | ')
        i += 1
        for item in col:
            print(item, end='')
        print()
"""
[T] [V]                     [W]    
[V] [C] [P] [D]             [B]    
[J] [P] [R] [N] [B]         [Z]    
[W] [Q] [D] [M] [T]     [L] [T]    
[N] [J] [H] [B] [P] [T] [P] [L]    
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9 
"""
stack = [ [], [], [], [], [], [], [], [], [] ]
stack[0].insert(0,'T')
stack[0].insert(0,'V')
stack[0].insert(0,'J')
stack[0].insert(0,'W')
stack[0].insert(0,'N')
stack[0].insert(0,'R')
stack[0].insert(0,'M')
stack[0].insert(0,'S')

stack[1].insert(0,'V')
stack[1].insert(0,'C')
stack[1].insert(0,'P')
stack[1].insert(0,'Q')
stack[1].insert(0,'J')
stack[1].insert(0,'D')
stack[1].insert(0,'W')
stack[1].insert(0,'B')

stack[2].insert(0,'P')
stack[2].insert(0,'R')
stack[2].insert(0,'D')
stack[2].insert(0,'H')
stack[2].insert(0,'F')
stack[2].insert(0,'J')
stack[2].insert(0,'B')

stack[3].insert(0,'D')
stack[3].insert(0,'N')
stack[3].insert(0,'M')
stack[3].insert(0,'B')
stack[3].insert(0,'P')
stack[3].insert(0,'R')
stack[3].insert(0,'F')

stack[4].insert(0,'B')
stack[4].insert(0,'T')
stack[4].insert(0,'P')
stack[4].insert(0,'R')
stack[4].insert(0,'V')
stack[4].insert(0,'H')

stack[5].insert(0,'T')
stack[5].insert(0,'P')
stack[5].insert(0,'B')
stack[5].insert(0,'C')

stack[6].insert(0,'L')
stack[6].insert(0,'P')
stack[6].insert(0,'R')
stack[6].insert(0,'J')
stack[6].insert(0,'B')

stack[7].insert(0,'W')
stack[7].insert(0,'B')
stack[7].insert(0,'Z')
stack[7].insert(0,'T')
stack[7].insert(0,'L')
stack[7].insert(0,'S')
stack[7].insert(0,'C')
stack[7].insert(0,'N')

stack[8].insert(0,'G')
stack[8].insert(0,'S')
stack[8].insert(0,'L')

for line in lines:
    inst = line.split(',')
    print(line)
    temp = []
    for i in range(int(inst[0])):
        temp.append(stack[int(inst[1]) - 1].pop())
    for i in reversed(range(len(temp))):
        stack[int(inst[2]) - 1].append(temp[i])

    print_stack(stack)