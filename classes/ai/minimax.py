import random
import math


class Game:
    def __init__(self, p1, p2, is_p1_turn=random.random() > 0.5):
        self.p1 = p1
        self.p2 = p2
        self.is_p1_turn = is_p1_turn

    def take_turn(self, action):
        new_game = Game(self.p1, self.p2, self.is_p1_turn)
        if self.is_p1_turn:
            new_game.p1, new_game.p2 = action(self.p1, self.p2)
        else:
            new_game.p2, new_game.p1 = action(self.p2, self.p1)
        new_game.is_p1_turn = not new_game.is_p1_turn
        return new_game

    def get_current_player_score(self):
        return self.p1 - self.p2 if self.is_p1_turn else self.p2 - self.p1

    def to_tuple(self):
        return self.p1, self.p2, self.is_p1_turn, self.get_current_player_score()

    def __str__(self):
        return "{:3d}:{:3d}({})".format(self.p1, self.p2, "P1" if self.is_p1_turn else "P2")


def end():
    pass


def action_1(player, opponent):
    return player + 35, opponent


def action_2(player, opponent):
    if player > 25:
        return (player - 25) * 3, opponent
    else:
        return math.ceil((player + 60) / 2), opponent


def action_3(player, opponent):
    return player * 2, opponent + 20


def action_4(player, opponent):
    return player % 100, opponent % 100


def greedy(game_state, all_actions, max_turn_limit):
    for i in range(0, max_turn_limit):
        act_scores = list(map(lambda act: (act, game_state.take_turn(act).get_current_player_score() -
                                           game_state.take_turn(act).get_current_player_score()), all_actions))
        print(act_scores)
        best_act = act_scores[0]
        for a_s in act_scores:
            if a_s[1] > best_act[1]:
                best_act = a_s
        game_state = game_state.take_turn(best_act[0])
        print("scores:", game_state.p1, game_state.p2)


def minimax(game_state, all_actions, history, turn, max_turn_limit):
    if turn > max_turn_limit:
        return [history + [(game_state.to_tuple(), end)]]
    branches = []
    for a in all_actions:
        branches = branches + minimax(game_state.take_turn(a), all_actions, history + [(game_state.to_tuple(), a)],
                                      turn + 1, max_turn_limit)
    return branches


def minimax_agent(game_state, is_min_turn, all_actions, history, turn, max_turn_limit):
    if turn >= max_turn_limit:
        return end, game_state.get_current_player_score()
    best = end
    if is_min_turn:
        best_score = math.inf
    else:
        best_score = -math.inf
    for act in all_actions:
        new_act = minimax_agent(game_state.take_turn(act), not is_min_turn, all_actions, history +
                                [(game_state.to_tuple(), act)], turn + 1, max_turn_limit)
        if is_min_turn and (new_act[1] < best_score):
            best = act
            best_score = new_act[1]
        elif not is_min_turn and (new_act[1] > best_score):
            best = act
            best_score = new_act[1]
    return best, best_score


def explore_all_actions(game, all_actions, current_turn, max_turn_limit):
    res = minimax(game, all_actions, [], current_turn, max_turn_limit)
    res = list(map(lambda r: list(
        map(lambda p: "p1: {}. p2: {}. next {}".format(p[0][0], p[0][1], p[1].__name__), r)), res))
    print(*res, sep="\n")


def play_game(game, all_actions, current_turn, max_turn_limit):
    print(explore_all_actions(game, all_actions, current_turn, max_turn_limit))

    while current_turn < max_turn_limit:
        print("current state: turn {}. p1 score: {}. p2 score: {}. Your turn.".format(current_turn, game.p1, game.p2))
        a = input("action (1,2, ...)?")
        if a == "1" and action_1 in all_actions:
            game = game.take_turn(action_1)
        elif a == "2" and action_2 in all_actions:
            game = game.take_turn(action_2)
        elif a == "3" and action_3 in all_actions:
            game = game.take_turn(action_3)
        elif a == "4" and action_4 in all_actions:
            game = game.take_turn(action_4)
        else:
            print("try again")
            continue
        current_turn = current_turn + 1
        if current_turn > max_turn_limit:
            break
        print(
            "current state: turn {}. p1 score: {}. p2 score: {}. Enemy's turn.".format(current_turn, game.p1, game.p2))
        result = minimax_agent(game, True, all_actions, [], current_turn, max_turn_limit)
        print("Enemy takes:", result[0].__name__)
        game = game.take_turn(result[0])
        current_turn = current_turn + 1
    print("Game ended: turn {}. p1 score: {}. p2 score: {}.".format(current_turn, game.p1, game.p2))
    if game.p1 > game.p2:
        print("you win")
    elif game.p1 < game.p2:
        print("you lose")
    else:
        print("draw")


max_turn = 4
g = Game(50, 50, True)
actions = [action_1, action_2]
play_game(g, actions, 0, max_turn)
