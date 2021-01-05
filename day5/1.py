#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_input(path):

    with open(path, 'r') as f:
        seatCodes = f.readlines()
        seatCodes = [line.strip() for line in seatCodes]
    return seatCodes

def decode_seatID(seatCode):
    #decode seat row

    #prepare list 0-127 for row check
    rows = []
    i = 0 
    for i in range(0,128,1):
        rows.append(i)
    #parse first 7 chars from seatCode
    seatCodeRow = seatCode[:7]

    i = 0    
    for letter in seatCodeRow:
        if i == 0:
            updatedRowList = check_half_row(letter, rows)
            i+=1
        else:
            updatedRowList = check_half_row(letter, updatedRowList)
    #row
    rowNumber = updatedRowList[0]

    #decode seat column
    #prepare list 0-8 for column check
    cols = []
    i = 0 
    for i in range(0,8,1):
        cols.append(i)
    
    #parse first 7 chars from seatCode
    seatCodeCol = seatCode[7:]

    i = 0    
    for letter in seatCodeCol:
        if i == 0:
            updatedColList = check_half_row(letter, cols)
            i+=1
        else:
            updatedColList = check_half_row(letter, updatedColList)

    colNumber = updatedColList[0]

    #calculate seat id
    seatID = rowNumber * 8 + colNumber

    return seatID

def check_half_row(letter, rowList):
    updatedRowList = []
    if letter == 'F' or letter == 'L':
        updatedRowList = rowList[:(int(len(rowList)/2))]
    elif letter == 'B' or letter == 'R':
        updatedRowList = rowList[(int(len(rowList)/2)):]
    return updatedRowList


def main():
    path = 'input.txt'
    seatCodes = parse_input(path)
    
    seatIdList = []
    for code in seatCodes:
        seatIdList.append(int(decode_seatID(code)))

    print('part 1: max seatID:',max(seatIdList))

    #part2
    seatIdMin = min(seatIdList)
    seatIdMax = max(seatIdList)
    seatIdList_sorted = sorted(seatIdList)
    
    i = 0

    for i in range(seatIdMin, seatIdMax+1):
        if i != seatIdList_sorted[i-seatIdMin]:
            print('missing ID:', i)
            break

    


if __name__=='__main__':
    main()