from itertools import permutations

digits = input("Enter the 4 digits you know (eg... 3214)")

possible_keys = permutations(list(digits))

print("\n")

for x in possible_keys:
    print("".join(x))