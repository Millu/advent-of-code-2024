import regex as re


def day3_pt1(file):

    sum = 0
    regex_to_find_multiples = 'mul\(\d{1,3},\d{1,3}\)'
    matches = []
    with open (file, 'r') as file:
        for line in file:
            matches.extend(re.findall(regex_to_find_multiples, line))

    for i in matches:
        numbers = re.findall('([0-9]*)', i)
        numbers[:] = [x for x in numbers if x]
        sum += int(numbers[0]) * int(numbers[1])
        
    print('Sum:', sum)        

def day3_pt2(file):
    sum = 0
    matches = []

    regex_to_find_multiples = 'mul\(\d{1,3},\d{1,3}\)'
    regex_do = 'do\(\)'
    regex_dont = "don't\(\)"

    with open (file, 'r') as file:
        for line in file:
             matches.extend(re.findall(regex_to_find_multiples+'|'+regex_do+'|'+regex_dont, line))

    enabled = True
    for i in matches:
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        elif enabled and 'mul' in i:
            numbers = re.findall('([0-9]*)', i)
            numbers[:] = [x for x in numbers if x]
            sum += int(numbers[0]) * int(numbers[1])

    print('Sum:', sum)

if __name__ == "__main__":
    file_name = 'day3.txt'
    day3_pt1(file_name)
    day3_pt2(file_name)