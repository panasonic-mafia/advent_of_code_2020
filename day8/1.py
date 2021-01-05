def part_1(path):
    with open(path, 'r') as f:
        code = [line.strip() for line in f.readlines()]

        parsed_code = []
        for line in code:
            mydict = {}
            a = line.split(" ")
            mydict[a[0]] = a[1]
            mydict['run'] = 0
            parsed_code.append(mydict)

        #run code
        accumulator = 0
        for i in range(0, len(parsed_code), 1):
            while parsed_code[i]['run'] != 1:
                parsed_code[i]['run'] = 1
                command = list(parsed_code[i].keys())[0]
                value = int(parsed_code[i][command])
                if command == 'acc':
                    accumulator += value
                    i += 1
                elif command == 'jmp':
                    if value > 0:
                        i += value
                    else:
                        i += value
                elif command == 'nop':
                    i += 1
                print (i, command, value, accumulator)
            break
        return accumulator





    

def part_2(path):
    with open(path, 'r') as f:
        code = [line.strip() for line in f.readlines()]

        parsed_code = []
        for line in code:
            mydict = {}
            a = line.split(" ")
            mydict[a[0]] = a[1]
            mydict['run'] = 0
            parsed_code.append(mydict)

        parsed_code[518]['nop'] = parsed_code[518]['jmp']
        del parsed_code[518]['jmp']

        #run code
        accumulator = 0
        for i in range(0, len(parsed_code), 1):
            while parsed_code[i]['run'] != 1:
                parsed_code[i]['run'] = 1
                command = list(sorted(parsed_code[i].keys()))[0]
                value = int(parsed_code[i][command])
                if command == 'acc':
                    accumulator += value
                    i += 1
                elif command == 'jmp':
                    if value > 0:
                        i += value
                    else:
                        i += value
                elif command == 'nop':
                    i += 1
                print (i, command, value, accumulator)
            break
        return accumulator


def main():
    print('part 1:', part_1('input.txt'))
    print('part 2:', part_2('input.txt'))
    

if __name__=="__main__":
    main()