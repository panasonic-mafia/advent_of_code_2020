#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
task:

Given matrix like this:

.#..........#......#..#.....#..
....#.............#.#....#..#..
.....##...###....#..#.......#..
.#....#..#......#........#.....
.#.........###.#..........##...
...............##........#.....
#..#..........#..##..#....#.#..

Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
how many # would you encounter?

'''


def read_input(path):
    '''
    read and parse input like below:
        .#.....
        ....#..

    output into two-dimentional list:
        [[.#.....], [....#..]]
    '''

    m = open(path, 'r')
    outlist = m.readlines()
    outlist = [line.strip() for line in outlist]
    #expand list to the right with same values
    outlist = [line*100 for line in outlist]

    return outlist

def calculate_trees(a: list, row_step: int, col_step: int):
    
    i = 0
    j = 0

    threes = 0
    for i in range(0,len(a),row_step):
        # print('i:',i)
        # print('j:',j)
        if i == 0 and j ==0:
            j+=col_step
        else:
            if a[i][j] == '#':
                threes+=1
            j+=col_step


    return threes

def main():
    input_path = 'input.txt'
    parsed_list = read_input(input_path)

    # Right 1, down 1.
    threes_1_1 = calculate_trees(parsed_list, 1, 1)
    print('Right 1, down 1:', threes_1_1)

    # Right 3, down 1. (This is the slope you already checked: 247)
    threes_3_1 = calculate_trees(parsed_list, 1, 3)
    print('Right 3, down 1:',threes_3_1)

    # Right 5, down 1.
    threes_5_1 = calculate_trees(parsed_list, 1, 5)
    print('Right 5, down 1:',threes_5_1)

    # Right 7, down 1.
    threes_7_1 = calculate_trees(parsed_list, 1, 7)
    print('Right 7, down 1:',threes_7_1)

    # Right 1, down 2.
    threes_1_2 = calculate_trees(parsed_list, 2, 1)
    print('Right 1, down 2:',threes_1_2)

    print('answer: ', (threes_1_1*threes_3_1*threes_5_1*threes_7_1*threes_1_2))
    

if __name__=="__main__":
    main()