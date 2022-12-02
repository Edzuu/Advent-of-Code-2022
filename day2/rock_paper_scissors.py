def opponent(selection):
    if selection == "A":
        return 1
    elif selection == "B":
        return 2
    elif selection == "C":
        return 3

def you(selection):
    if selection == "X":
        return 1
    elif selection == "Y":
        return 2
    elif selection == "Z":
        return 3

def you_updated(him, you):
    if you == "Z":
        if him == 3:
            return 1
        else:
            return him + 1
    elif you == "Y":
        return him
    elif you == "X":
        if him == 1:
            return 3
        else:
            return him - 1

score = 0

#Part 1
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        o = opponent(line[0])
        y = you(line[2])
        if o == y:
            score += 3 + y
        elif o == 1 and y == 2:
            score += 6 + y
        elif o == 3 and y == 1:
            score += 6 + y
        elif o == 2 and y == 3:
            score += 6 + y
        else:
            score += y

print(score)

score_updated = 0

#Part 2
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        o = opponent(line[0])
        y = you_updated(o, line[2])
        if o == y:
            score_updated += 3 + y
        elif o == 1 and y == 2:
            score_updated += 6 + y
        elif o == 3 and y == 1:
            score_updated += 6 + y
        elif o == 2 and y == 3:
            score_updated += 6 + y
        else:
            score_updated += y

print(score_updated)