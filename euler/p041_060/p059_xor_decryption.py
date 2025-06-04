from collections import Counter

with open("../data/p059_cipher.txt") as f:
    original_chars = [int(_) for _ in f.readline().split(",")]
    print(original_chars)

    chars = [[c for i, c in enumerate(original_chars) if i % 3 == 0],
             [c for i, c in enumerate(original_chars) if i % 3 == 1],
             [c for i, c in enumerate(original_chars) if i % 3 == 2]]

    # find most occurred characters
    freq = [sorted(list(Counter(clist).items()), key=lambda _: _[1], reverse=True) for clist in chars]
    space_chars = [_[0][0] for _ in freq]
    keys = [_ ^ 32 for _ in space_chars]  # 32 is the space characters
    chars_xor = [_ ^ keys[i % 3] for i, _ in enumerate(original_chars)]
    chars_decoded = [chr(_) for _ in chars_xor]
    print("".join(chars_decoded))
    print(sum(chars_xor))
