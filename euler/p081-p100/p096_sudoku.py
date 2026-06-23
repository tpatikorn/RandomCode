from typing import Dict, Tuple, List, Set

from euler.util import get_euler_data_filepath


class Cell:
    def __init__(self, row: int, col: int, value: int, potentials: Set[int]):
        self.__row = row
        self.__col = col
        self.__value = value
        self.__potentials = potentials

    def __repr__(self):
        return f"({self.__row},{self.__col}): {self.__value} {self.__potentials if self.__potentials else ''}"

    def get_value(self):
        return self.__value

    def set_value(self, value: int):
        if self.__value == 0:
            self.__value = value
            self.__potentials = set()
        else:
            raise RuntimeError("trying to override value of existing cell", self.__repr__(), value)

    def set_value_last_potential(self):
        if len(self.__potentials) == 1:
            self.__value = self.__potentials.pop()
            self.__potentials = set()
            return self.__value
        else:
            raise RuntimeError("potential length is not 1", self.__repr__())

    def set_potentials(self, potentials: Set[int]):
        if self.__value == 0 and len(self.__potentials) == 0:
            self.__potentials = potentials
        else:
            raise RuntimeError("can't set potentials for existing cell", self.__repr__())

    def remove_potential(self, value: int):
        self.__potentials = self.__potentials - {value}
        if self.__value == 0 and len(self.__potentials) == 0:
            raise RuntimeError("bad potential removal", self.__repr__(), value)

    def get_potentials(self):
        return self.__potentials


class Sudoku:
    def __init__(self, grid: List[List[int]]) -> None:
        self.grid: List[List[Cell]] = [[Cell(-1, -1, 0, set()) for _ in r] for r in grid]
        for row in range(9):
            for col in range(9):
                self.grid[row][col] = Cell(row, col, grid[row][col], set())

        for row in range(9):
            for col in range(9):
                if self.grid[row][col].get_value() == 0:
                    potentials = ({1, 2, 3, 4, 5, 6, 7, 8, 9} - self.get_neighbors(row, col))
                    self.grid[row][col].set_potentials(potentials)

    def get_neighbors(self, row: int, col: int, where="all"):
        match where:
            case "row":
                return self._get_neighbors_row(row, col)
            case "col":
                return self._get_neighbors_col(row, col)
            case "cell":
                return self._get_neighbors_cell(row, col)
            case _:
                return (self._get_neighbors_row(row, col)
                        .union(self._get_neighbors_col(row, col))
                        .union(self._get_neighbors_cell(row, col)))

    def _get_neighbors_row(self, row: int, col: int):
        vals = {_.get_value() for _ in self.grid[row]}
        return set(vals) - {0}

    def _get_neighbors_col(self, row: int, col: int):
        vals = {_.get_value() for _ in [_r[col] for _r in self.grid]}
        return set(vals) - {0}

    def _get_neighbors_cell(self, row: int, col: int):
        cell_row = row // 3
        cell_col = col // 3
        cell = self.grid[cell_row * 3: cell_row * 3 + 3]
        vals = [_[cell_col * 3: cell_col * 3 + 3] for _ in cell]
        flatten = {_v.get_value() for _ in vals for _v in _}
        return set(flatten) - {0}

    def print_grid(self):
        print(*[[_.get_value() for _ in row] for row in self.grid], sep="\n")

    def add_new_number(self, row: int, col: int, new_number: int):
        self.grid[row][col].set_value(new_number)
        self.remove_neighbor_potential(row, col, new_number)

    def remove_neighbor_potential(self, row: int, col: int, to_remove: int):
        for g_row in range(9):
            for g_col in range(9):
                if ((row == g_row) or (col == g_col) or
                        ((row // 3 == g_row // 3) and (col // 3 == g_col // 3))):
                    self.grid[g_row][g_col].remove_potential(to_remove)

    def solve_attempt(self, n_rounds=50):
        for _ in range(n_rounds):
            changed = False
            # print("Attempting to solve. round", _)
            if self.is_solved():
                # print("Solved!")
                # self.print_grid()
                return True

            # check row
            for row in range(9):
                potential_track = [[] for _ in range(10)]
                for col in range(9):
                    for _e in self.grid[row][col].get_potentials():
                        potential_track[_e].append((row, col))

                for i in range(1, 10):
                    if len(potential_track[i]) == 1:
                        new_number = i
                        target_row = potential_track[i][0][0]
                        target_col = potential_track[i][0][1]
                        self.add_new_number(target_row, target_col, new_number)
                        # print(f"found a new number: {new_number} at ({target_row}, {target_col}) by check row")
                        changed = True
                        # break immediately since potential_track could change unpredictably after cell change
                        break

            # check col
            for col in range(9):
                potential_track = [[] for _ in range(10)]
                for row in range(9):
                    for _e in self.grid[row][col].get_potentials():
                        potential_track[_e].append((row, col))

                for i in range(1, 10):
                    if len(potential_track[i]) == 1:
                        new_number = i
                        target_row = potential_track[i][0][0]
                        target_col = potential_track[i][0][1]
                        self.add_new_number(target_row, target_col, new_number)
                        # print(f"found a new number: {new_number} at ({target_row}, {target_col}) by check col")
                        changed = True
                        # break immediately since potential_track could change unpredictably after cell change
                        break

            # check cell
            for cell in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
                potential_track: Dict[int, List[Tuple[int, int]]] = {_: [] for _ in range(1, 10)}
                for pos in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
                    row = cell[0] + pos[0]
                    col = cell[1] + pos[1]
                    if self.grid[row][col].get_value() == 0:
                        for n in self.grid[row][col].get_potentials():
                            potential_track[n].append((row, col))
                for pt in potential_track.keys():
                    if len(potential_track[pt]) == 1:
                        new_number = pt
                        target_row = potential_track[pt][0][0]
                        target_col = potential_track[pt][0][1]
                        self.add_new_number(target_row, target_col, new_number)
                        changed = True
                        # print(f"found a new number: {new_number} at ({target_row}, {target_col}) by check cell")
                        # break immediately since potential_track could change unpredictably after cell change
                        break

            # last num standing
            for row in range(9):
                for col in range(9):
                    if len(self.grid[row][col].get_potentials()) == 1:
                        new_number = self.grid[row][col].set_value_last_potential()
                        self.remove_neighbor_potential(row, col, new_number)
                        # print(f"found a new number: {new_number} at ({row}, {col}) by last potential")
                        changed = True
                        break
            if not changed:
                # print("No changes made, attempting trial and error")
                val_only = [[_c.get_value() for _c in _r] for _r in self.grid]
                try_attempt_left = 10
                for try_row in range(9):
                    for try_col in range(9):
                        if self.grid[try_row][try_col].get_value() == 0:
                            for try_potential in self.grid[try_row][try_col].get_potentials():
                                simulated_grid = Sudoku(val_only)
                                simulated_grid.add_new_number(try_row, try_col, try_potential)
                                simulated_grid.remove_neighbor_potential(try_row, try_col, try_potential)
                                try:
                                    simulated_grid.solve_attempt(50)
                                    self.grid = simulated_grid.grid
                                except RuntimeError:
                                    self.grid[try_row][try_col].remove_potential(try_potential)
                                    try_attempt_left -= 1
                        if try_attempt_left <= 0:
                            # this is a more expensive operation, so use it sparingly
                            break
                    if try_attempt_left <= 0:
                        # this is a more expensive operation, so use it sparingly
                        break



    def is_solved(self):
        all_vals = [[_v.get_value() for _v in _] for _ in self.grid]
        for row_val in all_vals:
            if set(row_val) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
        for col_index in range(0, 9):
            col_vals = set()
            for row_val in all_vals:
                col_vals.add(row_val[col_index])
            if col_vals != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
        return True



grids = []

with open(get_euler_data_filepath("p096_sudoku.txt")) as f:
    _grid = []
    for line in f:
        if line[0:4] == "Grid":
            if len(_grid) > 0:
                grids.append(Sudoku(_grid))
            _grid = []
        else:
            _grid.append([int(_) for _ in line[0:9]])
    grids.append(Sudoku(_grid))

sum_top_left = 0
ct = 0
for g in grids:
    g.solve_attempt(50)
    if g.is_solved():
        print("Solved!")
    else:
        raise RuntimeError("bad bad bad")
    # g.print_grid()
    top_left = g.grid[0][0].get_value() * 100 + g.grid[0][1].get_value() * 10 + g.grid[0][2].get_value()
    print(top_left)
    sum_top_left += top_left
    ct += 1
print("sum = ", sum_top_left, ct)