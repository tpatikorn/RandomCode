print(73162890)  # by using excel lol

orig_rel = set()
with open("../data/p079_passcodes.txt") as data:
    for line in data:
        orig_rel.add((line[0], line[1]))
        orig_rel.add((line[1], line[2]))

rel = list(orig_rel)
rel.sort()
print(rel)

did_change = True
ordered_front = []
ordered_back = []
while did_change:
    did_change = False
    front = {_[0] for _ in rel}
    back = {_[1] for _ in rel}
    # front no back
    if len(front - back) > 0:
        did_change = True
        ordered_front += list(front - back)
        rel = [_ for _ in rel if _[0] not in front - back]
    front = {_[0] for _ in rel}
    back = {_[1] for _ in rel}
    if len(back - front) > 0:
        did_change = True
        ordered_back = list(back - front) + ordered_back
        rel = [_ for _ in rel if _[1] not in back - front]

ans = "".join(ordered_front + ordered_back)
print(ans)
print("leftover", rel)
print([_ for _ in orig_rel if _[0] not in set(ans) or _[1] not in set(ans)])