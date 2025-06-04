from collections import Counter

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# J,Q,K,A = 11, 12, 13, 14
# 8: straight flush (highest card)
# 7: 4kind      (card, leftover)
# 6: FH         (3kind, 2kind)
# 5: flush      (highest to lowest)
# 4: straight   (highest to lowest)
# 3: 3k         (3kind, 1high, 1low)
# 2: 2pairs     (2high, 2low, 1)
# 1: 1pair      (2, 1high, 1mid, 1low)
# 0: single     (highest to lowest)

STRAIGHT_FLUSH = 8
FOUR_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
SINGLE = 0


def calculate_hand_rank(hand: list[str]):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    suits = [_[1] for _ in hand]
    cards = [_[0] for _ in hand]
    cards = [10 if _ == "T" else
             11 if _ == "J" else
             12 if _ == "Q" else
             13 if _ == "K" else
             14 if _ == "A" else
             int(_) for _ in cards]
    # flush check
    cards = sorted(cards)
    counter = sorted(list(Counter(cards).items()), key=lambda kv: kv[1] + kv[0] / 20, reverse=True)
    card_value_sorted = [_[0] for _ in counter]
    highest_rank = SINGLE
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        highest_rank = FLUSH
    if cards[0] == cards[1] - 1 == cards[2] - 2 == cards[3] - 3 == cards[4] - 4:
        if highest_rank == FLUSH:
            highest_rank = STRAIGHT_FLUSH
        else:
            highest_rank = STRAIGHT

    # sort by count, then sort by number
    if counter[0][1] == 4:
        highest_rank = FOUR_KIND
    elif counter[0][1] == 3 and counter[1][1] == 2:
        highest_rank = FULL_HOUSE
    elif counter[0][1] == 3:
        highest_rank = THREE_KIND
    elif counter[0][1] == 2 and counter[1][1] == 2:
        highest_rank = TWO_PAIR
    elif counter[0][1] == 2:
        highest_rank = ONE_PAIR
    return highest_rank, card_value_sorted


def rank_two_hands(hands: str):
    hands = hands.split()
    hand_l = hands[0: 5]
    hand_r = hands[5: 10]
    print(hand_l, hand_r)
    rank_l = calculate_hand_rank(hand_l)
    rank_r = calculate_hand_rank(hand_r)
    print(hands, rank_l, rank_r)
    if rank_l[0] > rank_r[0]:
        return "l"
    elif rank_r[0] > rank_l[0]:
        return "r"
    else:
        for (card_l, card_r) in zip(rank_l, rank_r):
            if card_l > card_r:
                return "l"
            elif card_r > card_l:
                return "r"
            else:
                continue
    return "0"


l_win = 0
r_win = 0
draw = 0
with open("../data/p054_poker.txt") as poker:
    for line in poker:
        result = rank_two_hands(line)
        match result:
            case "l":
                l_win += 1
            case "r":
                r_win += 1
            case _:
                draw += 1

print(l_win, r_win, draw)

while True:
    try:
        hand = input("Enter a hand: ")
        print(rank_two_hands(hand))
    except:
        print("Invalid input")