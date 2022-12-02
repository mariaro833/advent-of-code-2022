import os
import numpy as np
import re

working_directory = os.getcwd()

def main():
    elfs = []
    f = open(r"day-1\input.txt", mode='r', encoding='utf-8')
    list = f.read()
    f.close
    s_max = 0
    elfs = re.split('\n\n', list)
    for i in range (len(elfs)):
        sum_act = sum(map(int, elfs[i].split('\n')))
        if sum_act > s_max:
            s_max = sum_act
    print (s_max)


if __name__ == "__main__":
    main()
