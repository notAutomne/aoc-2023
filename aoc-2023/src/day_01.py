"""Day 01 AoC 2023"""
import re

DICT_NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10 }

PATTERN = r"(?=(one|two|three|four|five|six|seven|eight|nine|ten|\d))"


def part_01(challenge: str) -> int:
    count = 0

    for line in challenge.split("\n"):
        for word, initial in DICT_NUMBERS.items():
            line = line.replace(word, str(initial))
        templine = [int(c) for c in line if c.isdigit()]
        count += templine[0]*10 + templine[-1]

    return count

def get_answer(challenge: str) -> int:
    count = 0

    for line in challenge.split("\n"):
        result = re.findall(PATTERN, line)
        possible_answers = [(int(x) if x.isdigit() else DICT_NUMBERS[x]) for x in result]
        print (possible_answers)
        count += possible_answers[0]*10 + possible_answers[-1]

    return count
