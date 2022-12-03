import string

sum = 0

#Part 1
with open("input.txt") as file:
    for line in file:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        sorted=list(set(firstpart)&set(secondpart))
        for letter in sorted:
            sum += string.ascii_letters.index(letter) + 1

print(sum)

#Part 2
count = 0
sum = 0
array = []

with open("input.txt") as file:
    strings = file.read().splitlines()
    for line in strings:
        if count == 0:
            first = line
            count += 1
        elif count == 1:
            second = line
            count += 1
        elif count == 2:
            third = line
            sorted=list(set(first)&set(second)&set(third))
            for letter in sorted:
                sum += string.ascii_letters.index(letter) + 1
            count = 0
        
print(sum)

