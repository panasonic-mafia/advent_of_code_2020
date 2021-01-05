#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
"""
Count the number of valid passports - those that have all required fields. 
Treat cid as optional.

fields:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

passport examples:
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in

"""

def list_to_dict(rlist):
    return dict(map(lambda s : map(str.strip, s.split(':')), rlist))

def read_input(input_path):
    """
    read and parse input txt to list of dicts containing passports
    """
    with open(input_path, 'r') as f:
        input_str = f.read()
    
    input_str = input_str.split('\n\n')
    
    mylist = []
    
    for line in input_str:
        objects = line.split()
        mylist.append(list_to_dict(objects))

    return mylist

def check_passport(passport: dict):
    """
    check if passport contains all fields, cid as optional
    """
    passport_mask = ['byr','iyr','eyr','hgt','hcl','pid','ecl']
    passport_mask_cid = ['byr','iyr','eyr','hgt','hcl','pid','ecl','cid']
    if (sorted(passport.keys()) == sorted(passport_mask)) or (sorted(passport.keys()) == sorted(passport_mask_cid)):
        return True
    else:
        return False


def check_passport_fields(passport: dict):
    """
    check if passport contains all fields and valid values, cid as optional
    """

    #Birth Year check
    if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
        #Issue Year check
        if int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
            #Expiration Year check
            if int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                #Height check
                #parse height to dict, then check
                height = re.search(r'^(\d+)(cm|in)$', passport['hgt'])
                if height:
                    heightDict = {'unit':height.group(2), 'value':height.group(1)}
                    if (heightDict['unit'] == 'cm' and int(heightDict['value']) >= 150 and int(heightDict['value']) <= 193) or (heightDict['unit'] == 'in' and int(heightDict['value']) >= 59 and int(heightDict['value']) <= 76):
                       # Hair color check
                       hairColor = re.search(r'^#[0-9a-f]{6}$', passport['hcl'])
                       if hairColor:
                           #Eye Color check
                           eyeColor = re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl'])
                           if eyeColor:
                               #passport id check
                               passportId = re.search(r'^(\d){9}$', passport['pid'])
                               if passportId:
                                   return True
    else:
        return False




def main():
    input_path = 'input.txt'
    a = read_input(input_path)
    c = 0 #count of valid passports
    for passport in a:
        if check_passport(passport) and check_passport_fields(passport):
            c+=1
    print('count of valid passports, first puzzle:',c)
    



    

if __name__=='__main__':
    main()
