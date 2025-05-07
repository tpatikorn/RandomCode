import random
from typing import List
from enum import Enum
from random import randint


class CType(Enum):
    GO = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    R = 10
    T = 20
    U = 30
    FP = 50
    JAIL = 60
    G2J = 70
    CC = 80
    CH = 90


class Cell:
    def __init__(self, cell_type: CType):
        self.type = cell_type

    def __repr__(self):
        return str(self.type)


class Monopoly:
    def __init__(self):
        self.position = 0
        self.board = [Cell(CType.GO),
                      Cell(CType.A), Cell(CType.CC), Cell(CType.A), Cell(CType.T), Cell(CType.R),
                      Cell(CType.B), Cell(CType.CH), Cell(CType.B), Cell(CType.B),
                      Cell(CType.JAIL),
                      Cell(CType.C), Cell(CType.U), Cell(CType.C), Cell(CType.C), Cell(CType.R),
                      Cell(CType.D), Cell(CType.CC), Cell(CType.D), Cell(CType.D),
                      Cell(CType.FP),
                      Cell(CType.E), Cell(CType.CH), Cell(CType.E), Cell(CType.E), Cell(CType.R),
                      Cell(CType.F), Cell(CType.F), Cell(CType.U), Cell(CType.F),
                      Cell(CType.G2J),
                      Cell(CType.G), Cell(CType.G), Cell(CType.CC), Cell(CType.G), Cell(CType.R),
                      Cell(CType.CH), Cell(CType.H), Cell(CType.T), Cell(CType.H)]
        self.board_size = len(self.board)
        self.counter = [0 for _ in self.board]
        self.lookup = {}
        for cell_index in range(self.board_size):
            if self.board[cell_index].type in self.lookup:
                self.lookup[self.board[cell_index].type].append(cell_index)
            else:
                self.lookup[self.board[cell_index].type] = [cell_index]
        self.CC_counter = 0
        self.CH_counter = 0

    def find_next_position(self, cell_type: CType):
        for _ in range(self.board_size):
            if self.board[(self.position + _) % self.board_size].type == cell_type:
                return (self.position + _) % self.board_size

    def find_specific(self, cell_type: CType, num=1):
        return self.lookup[cell_type][num - 1]

    def on_move_to(self, new_position):
        new_position = new_position % self.board_size
        match self.board[new_position].type:
            case CType.G2J:
                return self.on_move_to(self.find_specific(CType.JAIL))

            case CType.CC:
                self.CC_counter = (self.CC_counter + 1) % 16
                match self.CC_counter:
                    case 1:
                        return self.on_move_to(self.find_specific(CType.GO))
                    case 2:
                        return self.on_move_to(self.find_specific(CType.JAIL))

            case CType.CH:
                self.CH_counter = (self.CH_counter + 1) % 16
                match self.CH_counter:
                    case 1:
                        return self.on_move_to(self.find_specific(CType.GO))
                    case 2:
                        return self.on_move_to(self.find_specific(CType.JAIL))
                    case 3:
                        return self.on_move_to(self.find_specific(CType.C, 1))
                    case 4:
                        return self.on_move_to(self.find_specific(CType.E, 3))
                    case 5:
                        return self.on_move_to(self.find_specific(CType.H, 2))
                    case 6:
                        return self.on_move_to(self.find_specific(CType.R, 1))
                    case 7:
                        return self.on_move_to(self.find_next_position(CType.R))
                    case 8:
                        return self.on_move_to(self.find_next_position(CType.R))
                    case 9:
                        return self.on_move_to(self.find_next_position(CType.U))
                    case 10:
                        return self.on_move_to(new_position - 3)

        self.position = new_position
        self.counter[new_position] += 1
        return new_position

    def move_by(self, cell_count):
        return self.on_move_to(self.position + cell_count)


all_counter = None
monopoly = None
for repeat in range(10):
    print("doing #", repeat)
    monopoly = Monopoly()
    if all_counter is not None:
        monopoly.counter = all_counter
    for i in range(100_000):
        die1 = random.randint(1, 4)
        die2 = random.randint(1, 4)
        monopoly.move_by(die1 + die2)
    all_counter = monopoly.counter

print(*sorted(zip(enumerate(all_counter), monopoly.board),
              key=lambda x: x[0][1]), sep="\n")
