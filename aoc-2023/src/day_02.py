"""Day 02 AoC 2023"""
from typing import List

DAY = "02"

with open(
    f"aoc-2023/tests/day_02/day_02_challenge.txt",
    encoding="utf-8",
) as f:
    challenge = f.readlines()
    if challenge[-1] == "\n":
        challenge = challenge[:-1]


class GameSet:
    red: int = 0
    blue: int = 0
    green: int = 0

    def __repr__(self):
        return f"GameSet(red={self.red}, blue={self.blue}, green={self.green})"


class Game:
    id: int
    game_sets: List[GameSet] = []

    def line_parser(self, line_to_parse: str):
        self.id = int(line_to_parse.replace("Game ", "").split(":")[0])
        game_sets_p = line_to_parse.replace("\n", "").split(": ")[1].split("; ")
        for game_set in game_sets_p:
            colors = game_set.split(", ")
            gs = GameSet()
            for color in colors:
                color_name = color.split(" ")[1]
                color_value = int(color.split(" ")[0])
                match color_name:
                    case "red":
                        gs.red = color_value
                    case "blue":
                        gs.blue = color_value
                    case "green":
                        gs.green = color_value
            self.game_sets.append(gs)

    def __init__(self, line: str):
        self.game_sets = list()
        self.line_parser(line)

    def is_possible(self, mgs: GameSet) -> int:
        for game_set in self.game_sets:
            if game_set.red > mgs.red:
                return 0
            if game_set.blue > mgs.blue:
                return 0
            if game_set.green > mgs.green:
                return 0
        return self.id

    def set_value(self):
        max_red = 0
        max_blue = 0
        max_green = 0
        for game_set in self.game_sets:
            if game_set.red > max_red:
                max_red = game_set.red
            if game_set.blue > max_blue:
                max_blue = game_set.blue
            if game_set.green > max_green:
                max_green = game_set.green
        return max_red * max_blue * max_green

    def __repr__(self):
        return f"Game {self.id}: {self.game_set}"


part1 = 0
part2 = 0

master_gameset = GameSet()
master_gameset.red = 12
master_gameset.blue = 14
master_gameset.green = 13

games = []
for ln in challenge:
    games.append(Game(ln))

for game in games:
    part1 += game.is_possible(master_gameset)
    part2 += game.set_value()

print(part2)
