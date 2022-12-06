import re
import os

working_directory = os.getcwd()

def calc_priorities(c):
    if c.isupper():
        return ((ord(c)) - 38)
    else:
        return ((ord(c)) - 96)

def comp_half_string(list):
    sum = 0
    luggage = re.split('\n', list)
    n = 0
    for rucksack in luggage:
        i = 0
        items_to_check = []
        rucksack_1 = ""
        for item in rucksack:
            if i < len(rucksack) / 2:
                items_to_check.extend(item)
            else:
                rucksack_1 += rucksack_1.join(item)
            i += 1
        if len(items_to_check):
            sum += calc_priorities([elem for elem in set(items_to_check) if(elem in rucksack_1)][0])

def comp_three_lines(list):
    sum = 0
    luggage = re.split('\n', list)
    n = 0
    for rucksack in range(0, len(luggage)-1, 3):
        n = ''.join(set.intersection(*map(set, luggage[rucksack:rucksack + 3])))
        print (n)
        sum += calc_priorities(n)
    print (sum)

def main() -> None:
    f = open("day-3/input.txt", mode='r', encoding='utf-8')
    list = f.read()
    # comp_half_string(list)
    comp_three_lines(list)
    f.close

if __name__ == "__main__":
    main()
