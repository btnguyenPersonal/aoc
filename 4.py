#!/usr/bin/env python
with open('4input', 'r') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    ranges = line.strip().split(',')
    first = ranges[0].split('-')
    second = ranges[1].split('-')
    if int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        sum += 1
        # print(ranges)
        # print('.' * (int(first[0]) - 1) + 'A' * (int(first[1]) - int(first[0]) + 1))
        # print('.' * (int(second[0]) - 1) + 'B' * (int(second[1]) - int(second[0]) + 1))
    elif int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]):
        sum += 1
        # print(ranges)
        # print('.' * (int(first[0]) - 1) + 'A' * (int(first[1]) - int(first[0]) + 1))
        # print('.' * (int(second[0]) - 1) + 'B' * (int(second[1]) - int(second[0]) + 1))
    elif int(second[1]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        sum += 1
        # print(ranges)
        # print('.' * (int(first[0]) - 1) + 'A' * (int(first[1]) - int(first[0]) + 1))
        # print('.' * (int(second[0]) - 1) + 'B' * (int(second[1]) - int(second[0]) + 1))
    elif int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1]):
        sum += 1
        # print(ranges)
        # print('.' * (int(first[0]) - 1) + 'A' * (int(first[1]) - int(first[0]) + 1))
        # print('.' * (int(second[0]) - 1) + 'B' * (int(second[1]) - int(second[0]) + 1))
    else:
        print(ranges)
        print('.' * (int(first[0]) - 1) + 'A' * (int(first[1]) - int(first[0]) + 1))
        print('.' * (int(second[0]) - 1) + 'B' * (int(second[1]) - int(second[0]) + 1))
    # if (int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]) and int(first[1]) <= int(second[1])) or (int(first[0]) <= int(second[0]) and int(second[0]) <= int(first[1]) and int(first[1]) >= int(second[1])):
    #     sum += 1
    #     print(ranges)
    #     print('.' * int(first[0]) + 'A' * (int(first[1]) - int(first[0])))
    #     print('.' * int(second[0]) + 'B' * (int(second[1]) - int(second[0])))
    # else:
    #     print(ranges)
    #     print("INVALID")
    #     print('.' * int(first[0]) + 'A' * (int(first[1]) - int(first[0])))
    #     print('.' * int(second[0]) + 'B' * (int(second[1]) - int(second[0])))

print(sum)