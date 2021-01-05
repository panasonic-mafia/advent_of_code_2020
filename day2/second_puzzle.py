def parse_input(inputText):
    """
        parse input as dict e.g. 
        input is '1-3 a: abcde' 
        outdict should be {'lowNum': 1, 'highnum': 3, 'letter': 'a', 'password': 'abcde'}
    """

    outdict = []
    

    m = open(inputText, 'r')
    outlist = m.readlines()
    outlist = [line.strip() for line in outlist]

    for elem in outlist:
        elemdict = {}
        t = elem.split(' ')
        num = t[0].split('-')
        elemdict['lowNum'] = int(num[0])
        elemdict['highNum'] = int(num[1])
        elemdict['letter'] = t[1].replace(':','')
        elemdict['password'] = t[2]
        outdict.append(elemdict)

    return outdict


def check_password_first_puzzle(outdict):
    """
        returns True if given password is valid against given policy
        returns False if password is not valid

        The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
        For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
        e.g. '1-3 a: abcde' - is valid password 

    """

    from collections import Counter

    c = Counter(outdict['password'])
    if outdict['lowNum'] <= c[outdict['letter']] <= outdict['highNum']:
        return True
    else:
        return False


def check_password_second_puzzle(outdict):
    """
        returns True if given password is valid against given policy
        returns False if password is not valid

        Each policy describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
        Exactly one of these positions must contain the given letter. 
        Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
        e.g.    '1-3 a: abcde' is valid: position 1 contains a and position 3 does not.
                '2-9 c: ccccccccc' is invalid: both position 2 and position 9 contain c.
    """

    if bool(outdict['password'][outdict['lowNum']-1] == outdict['letter']) ^ bool(outdict['password'][outdict['highNum']-1] == outdict['letter']):
        return True
    else:
        return False

    pass


def main():
    inputpath = 'input.txt'
    outdict = parse_input(inputpath)
    print(outdict[0:3])

    i = 0
    j = 0

    for record in outdict:
        if check_password_first_puzzle(record) == True:
            i +=1
    print('passwords valid against first policy:', i)

    for record in outdict:
        if check_password_second_puzzle(record) == True:
            j += 1
    print('passwords valid against second policy:', j)

if __name__=='__main__':
    main()
