#Part 1
count = 0

string = open('input.txt', 'r').read()
start = string[:4]
print(start)
for char in range(0, len(string)):
    if len(set(start)) != 4:
        cropped = start[1:]
        start = cropped + string[char]
        count += 1
    elif len(set(start)) == 4:
        print(count)
        break

#Part 2
count = 0

string = open('input.txt', 'r').read()
start = string[:14]
for char in range(0, len(string)):
    if len(set(start)) != 14:
        cropped = start[1:]
        start = cropped + string[char]
        count += 1
    elif len(set(start)) == 14:
        print(count)
        break
