import math
import random


class XO:
    def __init__(self):
        self.board = [["_" for _ in range(0, 3)] for _ in range(0, 3)]
        self.turn = "X"

    def play(self, location):
        new_state = XO()
        new_state.board = [[elt for elt in row] for row in self.board]
        new_state.turn = self.turn
        x = location[0]
        y = location[1]
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print(x, y, "is out of range")
            return self, None
        if not new_state.board[x][y] == "_":
            print("location", x, y, "is occupied")
            return self, None
        new_state.board[x][y] = new_state.turn
        if new_state.turn == "X":
            new_state.turn = "O"
        else:
            new_state.turn = "X"
        return new_state, new_state.check_win()

    def get_actions(self):
        actions = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == "_":
                    actions.append((i, j))
        return actions

    def check_win(self):
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) \
                or (self.board[0][0] == self.board[1][1] == self.board[2][2]) \
                or (self.board[1][0] == self.board[1][1] == self.board[1][2]) \
                or (self.board[0][1] == self.board[1][1] == self.board[2][1]):
            if self.board[1][1] != "_":
                return self.board[1][1]
        elif (self.board[0][0] == self.board[1][0] == self.board[2][0]) \
                or (self.board[0][0] == self.board[0][1] == self.board[0][2]):
            if self.board[0][0] != "_":
                return self.board[0][0]
        elif (self.board[2][2] == self.board[2][1] == self.board[2][0]) \
                or (self.board[2][2] == self.board[1][2] == self.board[0][2]):
            if self.board[2][2] != "_":
                return self.board[2][2]
        else:
            return None

    def save_state(self):
        return "".join(map(lambda r: "".join(r), self.board))


def minimax(game_state, history, turn):
    branches = []
    for a in game_state.get_actions():
        new_game_state, result = game_state.play(a)
        if result:
            branches = branches + [history + [(new_game_state.save_state(), result + "win")]]
        else:
            branches = branches + minimax(new_game_state, history + [(new_game_state.save_state(), a)], turn + 1)
    return branches


equal_swap_chance = 0.3


def minimax_agent(game_state, min_turn_symbol, history, turn):
    best = None
    is_min_turn = game_state.turn == min_turn_symbol
    if is_min_turn:
        best_score = math.inf
    else:
        best_score = -math.inf
    if len(game_state.get_actions()) == 0:
        return None, 0
    for act in game_state.get_actions():
        new_game_state, result = game_state.play(act)
        if result:
            return act, -1 if game_state.turn == min_turn_symbol else 1
        else:
            _, new_score = minimax_agent(new_game_state, min_turn_symbol,
                                         history + [(new_game_state.save_state(), act)], turn + 1)
            if new_score == best_score and random.random() > equal_swap_chance:
                best = act
                best_score = new_score
            if is_min_turn and (new_score < best_score):
                best = act
                best_score = new_score
            elif not is_min_turn and (new_score > best_score):
                best = act
                best_score = new_score
    return best, best_score


if __name__ == "__main__":
    # game = XO()
    # print(game.save_state())
    # minimax_result = minimax(game, [], 0)
    # print(*minimax_result, sep="\n")

    game = XO()
    while True:
        try:
            print(*game.board, sep="\n")
            print(game.turn, "'s turn")
            if game.turn == 'X':
                next_location, _ = minimax_agent(game, "X", [], 0)
            else:
                loc = input("Your move?")
                if len(loc) == 1:
                    next_location = (math.floor((int(loc)) / 3), (int(loc)) % 3)
                else:
                    next_location = (int(loc[0]), int(loc[1]))
            game, res = game.play(next_location)
            if res:
                print(*game.board, sep="\n")
                print(res, " wins")
                break
            if len(game.get_actions()) == 0:
                print(*game.board, sep="\n")
                "draw!"
                break
        except Exception as e:
            print("invalid move, try again")
