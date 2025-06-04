from typing import List
from enum import Enum


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

    def find_next_position(self, current_position: int, cell_type: CType):
        for i in range(self.board_size):
            if self.board[(current_position + i) % self.board_size].type == cell_type:
                return i % self.board_size

    def find_specific(self, cell_type: CType, num=1):
        ct = 0
        for i, cell in enumerate(self.board):
            if cell.type == cell_type:
                ct += 1
                if ct == num:
                    return i
        raise RuntimeError("we're fucked!", cell_type, num)

    def compute_move(self, die_size=6):
        result = [0 for _ in range(self.board_size)]

        for old_position in range(self.board_size):
            for die_result in range(1, die_size + 1):
                new_position = (old_position + die_result) % self.board_size

                match self.board[new_position].type:
                    case CType.G2J:
                        result[self.find_specific(CType.JAIL)] += (1 / die_size)

                    case CType.CC:
                        result[self.find_specific(CType.GO)] += (1 / die_size) * (1 / 16)
                        result[self.find_specific(CType.JAIL)] += (1 / die_size) * (1 / 16)
                        result[new_position] += (1 / die_size) * (14 / 16)

                    case CType.CH:
                        result[self.find_specific(CType.GO)] += (1 / die_size) * (1 / 16)
                        result[self.find_specific(CType.JAIL)] += (1 / die_size) * (1 / 16)
                        result[self.find_specific(CType.C, 1)] += (1 / die_size) * (1 / 16)
                        result[self.find_specific(CType.E, 3)] += (1 / die_size) * (1 / 16)
                        result[self.find_specific(CType.H, 2)] += (1 / die_size) * (1 / 16)
                        result[self.find_specific(CType.R, 1)] += (1 / die_size) * (1 / 16)
                        result[self.find_next_position(new_position, CType.R)] += (1 / die_size) * (1 / 16)
                        result[self.find_next_position(new_position, CType.R)] += (1 / die_size) * (1 / 16)
                        result[self.find_next_position(new_position, CType.U)] += (1 / die_size) * (1 / 16)

                        if self.board[new_position - 3].type == CType.CC:
                            result[self.find_specific(CType.GO)] += (1 / die_size) * (1 / 16) * (1 / 16)
                            result[self.find_specific(CType.JAIL)] += (1 / die_size) * (1 / 16) * (1 / 16)
                            result[new_position] += (1 / die_size) * (1 / 16) * (14 / 16)
                        else:
                            result[new_position - 3] += (1 / die_size) * (1 / 16)
                        result[new_position] += (1 / die_size) * (6 / 16)

                    case _:
                        result[new_position] += 1 / die_size
        return result


monopoly = Monopoly()
cum_dist_result = monopoly.compute_move(8)
board_dist = [(a[0], a[1], b / sum(cum_dist_result)) for a, b in zip(enumerate(monopoly.board), cum_dist_result)]
board_dist.sort(key=lambda x: x[2])
print(*board_dist, sep='\n')
