#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def parse_input(input_path):
    with open(input_path, 'r') as f:
        input_str = f.read()
    
    input_str = input_str.split('\n\n')
    
    mylist = []
    
    for line in input_str:
        objects = line.split()
        mylist.append(objects)

    return mylist

def part1(mylist):
    output_sum = 0
    for group in mylist:
        merged_group = []
        for answer in group:
            merged_group += answer
        c = Counter(merged_group)
        output_sum += len(list(c))
    
    return output_sum

def part2(mylist):
    output_sum = 0
    for group in mylist:
        merged_group = []
        for answer in group:
            merged_group += answer
        c = Counter(merged_group)
        
        for item in c.items():
            if len(group) == item[1]:
                output_sum += 1

    return output_sum




def main():
    print(part1(parse_input('input.txt')))
    print(part2(parse_input('input.txt')))

if __name__=='__main__':
    main()