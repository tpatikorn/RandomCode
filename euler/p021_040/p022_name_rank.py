with open("../data/p022_names.txt", "r") as name_file:
    name_list = name_file.readline().replace("\"", "").split(sep=",")
    name_list.sort()


def string_to_val(s):
    encoded = s.encode()
    return sum(map(lambda e: e - 64, encoded))


print(string_to_val("COLIN"))

total = 0
for i in range(0, len(name_list)):
    print(i, name_list[i])
    total = total + string_to_val(name_list[i]) * (i + 1)
print(total)
