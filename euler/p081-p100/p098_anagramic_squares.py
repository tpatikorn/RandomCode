from math import sqrt

from euler.util import get_euler_data_filepath


def find_anagram_groups(word_list):
    letter_sets = {}
    for word in word_list:
        letter_list = list(word)
        letter_list.sort()
        letter_list = tuple(letter_list)
        if letter_list in letter_sets:
            letter_sets[letter_list].append(word)
        else:
            letter_sets[letter_list] = [word]
    _anagram_groups = {}
    for _k in letter_sets:
        if len(letter_sets[_k]) >= 2:
            _anagram_groups[_k] = letter_sets[_k]
    return _anagram_groups


def transfer_permutation(source, permuted, destination):
    source_map = {_k: _i for _i, _k in enumerate(source)}
    permuted_indices = [source_map[_] for _ in permuted]
    return [destination[_] for _ in permuted_indices]


square_list = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: []
}

for num in range(int(sqrt(1000)) - 10, int(sqrt(1_000_000_000)) + 10):  # all numbers that squared to 9 digits
    num_word = str(num * num)
    if len(num_word) != len(set(num_word)):
        continue
    square_list[len(num_word)].append(num_word)

with open(get_euler_data_filepath("p098_anagramic_squares.txt")) as f:
    words = f.readline().replace("\"", "").split(',')
    anagram_groups = find_anagram_groups(words)
    # biggest are 'INTRODUCE' and 'REDUCTION', 8 digits non-dupes

    for group in anagram_groups:
        group_members = anagram_groups[group]
        member0 = group_members[0]
        member1 = group_members[1]
        # there's one group with 3 members ['POST', 'SPOT', 'STOP'] but that's not a solution. I'm not checking for that
        print(member0, member1)
        for destination in square_list[len(member0)]:
            new_dest = "".join(transfer_permutation(member0, member1, destination))
            if new_dest in square_list[len(member0)]:
                print("EUREKA!", member0, member1, destination, new_dest)
