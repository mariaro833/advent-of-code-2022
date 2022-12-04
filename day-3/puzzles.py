import re

def calc_priorities(c):
    if c.isupper():
        return ((ord(c)) - 38)
    else:
        return ((ord(c)) - 96)

def comp_strings(list):
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
    print(sum)

def main() -> None:
    f = open(r"day-3\input.txt", mode='r', encoding='utf-8')
    list = f.read()
    comp_strings(list)
    f.close

if __name__ == "__main__":
    main()
