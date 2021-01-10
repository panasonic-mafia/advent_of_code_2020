
def parse_input(path):
    with open(path, 'r') as f:
        code = [int(line.strip()) for line in f.readlines()]
    return code

def part_1(series:list):
    invalid_number = 0
    for check_num in series:
        #skip preamble
        if series.index(check_num) > 24:

            #check if number is sum of two numbers from previous 25 numbers
            flag = 0
            i = 0
            num_slice = series[series.index(check_num)-25:series.index(check_num)]
            for num1 in num_slice:
                for num2 in num_slice[1:]:
                    if num1 != num2:
                        if check_num == num1+num2:
                            flag = 1
                            break
                i+=1
                if i == 25 and flag != 1:
                    invalid_number = check_num
                    break

        else:
            continue

    return invalid_number

def part_2(series:list, invalid_number):
        for i in range(0,len(series),1):
            for j in range(1,len(series),1):
                if sum(series[i:j]) == invalid_number:
                    a = sorted(series[i:j])[0]
                    b = sorted(series[i:j])[-1]
                    return a+b
                    


def main():
    num_series =parse_input('input.txt')
    invalid_number = part_1(num_series)
    print('part 1', part_1(num_series))
    print('part 2', part_2(num_series, invalid_number))

if __name__ == "__main__":
    main()