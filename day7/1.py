#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def parse_input(path):
    with open(path, 'r') as f:
        out = f.readlines()
        out = [line.strip() for line in out]
    
    return out

def dict_from_rules(rules:list):
    #create inner dicts on one level
    parsed_rules = {}
    for line in rules:
        if 'contain no other bags.' in line:
            a = line.split(' contain ')
            parsed_rules[a[0].replace(' bags','')] = ['']
        
        else:
            a = line.split(' contain ')
            
            if ',' in a[1]:
                b = a[1].split(', ')
                b = [line.replace('.','') for line in b]
                c = []
                for line in b:
                    x ={}
                    p = re.search(r'^(\d+)\s([a-z ]+)\sbags?$', line )
                    x[p[2]] = p[1]
                    c.append(x)
                parsed_rules[a[0].replace(' bags','')] = c
            else:
                b = a[1].strip('.')
                x = {}
                p = re.search(r'^(\d+)\s([a-z ]+)\sbags?$', b)
                x[p[2]] = p[1]
                parsed_rules[a[0].replace(' bags','')] = [x]
            
        
    return parsed_rules
            
            
def find_bag_part_1(all_rules, required_color):
    
    i = 0
    for key in all_rules.keys():
        if check_bag(all_rules, key, required_color):
            i+=1
        else:
            for elem in all_rules[key]:
                if check_bag(all_rules, elem, required_color):
                    i+=1
    return i


def find_bag_part_2(all_rules, requried_color):
    """
    find how many bags are inside bag with required_color
    """
    pass

def check_bag_2(all_rules, mykey, bag_count, used_keys_list):
    if (all_rules[mykey] != ['']) and (mykey not in used_keys_list):
        used_keys_list.append(mykey)
        # print(mykey,all_rules[mykey])
        for line in all_rules[mykey]:
            for a in line.values():
                bag_count += int(a)
            if line.keys():
                for k in line.keys():
                   bag_count+= check_bag_2(all_rules, k, bag_count, used_keys_list)
    
    return bag_count


def check_bag(all_rules, mykey, required_color):
    if required_color in all_rules[mykey]:
        return True
    else:
        for elem in all_rules[mykey]:
            if check_bag(all_rules, elem, required_color):
                    return True

def recreate_rules_dict(parsed_rules):
    new_dict={}
    for k in parsed_rules.keys():
        mylist = []
        for line in parsed_rules[k]:
            if line != '' and line != 'None':
                for lk in list(line.keys()):
                    mylist.append(lk)
        new_dict[k] = mylist
    return new_dict


def dict_for_part2(parsed_rules, my_key):
    for line in parsed_rules[my_key]:
        if parsed_rules[my_key] != ['']:
            # print(parsed_rules[my_key])
            for key in list(line.keys()):
                if (key != 'contains') and (parsed_rules[key] != ['']):
                    line['contains'] = parsed_rules[key]
                    dict_for_part2(parsed_rules,key)
    return parsed_rules

def bag_count_part_2(dict_for_part2, my_key):
    c = 0
    for line in dict_for_part2[my_key]:
        for key in list(line.keys()):
            if key != 'contains':
                buffkey = key
                c += int(line[key])
        for key in list(line.keys()):
            if key == 'contains':
                c += int(line[buffkey]) * bag_count_part_2(line, key)
    return c

def main():
    path = 'input.txt'
    rules = parse_input(path)
    parsed_rules = dict_from_rules(rules)
    new_dict = recreate_rules_dict(parsed_rules)
    print('part 1:', find_bag_part_1(new_dict, 'shiny gold'))  
    part2_dict = dict_for_part2(parsed_rules,'shiny gold')
    print('part 2', bag_count_part_2(part2_dict,'shiny gold'))
    

    

if __name__=='__main__':
    main()