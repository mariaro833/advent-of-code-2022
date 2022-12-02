import os
import re

working_directory = os.getcwd()

def find_max_3(list):
    sums = []
    elfs = re.split('\n\n', list)
    for elf in elfs:
        sums.extend([(sum(map(int, elf.split('\n'))))])
    print(sum(sorted(sums, reverse=True)[0:3]))


def find_max(list):
    s_max = 0
    elfs = re.split('\n\n', list)
    for elf in elfs:
        sum_act = sum(map(int, elf.split('\n')))
        if sum_act > s_max:
            s_max = sum_act
    # print(s_max)


def main() -> None:
    f = open(r"day-1\input.txt", mode='r', encoding='utf-8')
    list = f.read()
    find_max(list)
    find_max_3(list)
    f.close


if __name__ == "__main__":
    main()
