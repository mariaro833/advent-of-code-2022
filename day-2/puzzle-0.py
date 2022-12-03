import os
import re

working_directory = os.getcwd()

def calc_score_2(list):
    list = list.replace("A", "1")
    list = list.replace("B", "2")
    list = list.replace("C", "3")
    game = re.split('\n', list)
    score = 0
    for round in game:
        if len(round):
            a_0 = int(round[0])
            a_1 = round[2]
            # score += a_1
            if a_1 == "X":
                score += a_0 - 1
                if a_0 - 1 == 0:
                    score += 3
            elif a_1 == "Y":
                score += 3 + a_0
            else:
                if a_0 == 3:
                    score += 6 + 1
                else:
                    score += 6 + a_0 + 1     
    print (score)

def calc_score(list):
    list = list.replace("Z", "C")
    list = list.replace("Y", "B")
    list = list.replace("X", "A")
    list = list.replace("A", "1")
    list = list.replace("B", "2")
    list = list.replace("C", "3")
    game = re.split('\n', list)
    score = 0
    for round in game:
        if len(round):
            a_0 = int(round[0])
            a_1 = int(round[2])
            score += a_1
            if a_1 == a_0:
                score += 3
            elif (a_1 - a_0 == 1 or a_1 - a_0 == -2):
                score += 6
    print (score)


def main() -> None:
    f = open(r"day-2\input.txt", mode='r', encoding='utf-8')
    list = f.read()
    calc_score_2(list)
    f.close


if __name__ == "__main__":
    main()
