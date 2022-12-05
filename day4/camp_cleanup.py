count = 0

#Part 1
with open("input.txt") as file:
    strings = file.read().splitlines()
    for line in strings:
        partitioned_string = line.partition(',')

        first_elf = partitioned_string[0]
        second_elf = partitioned_string[2]

        partitioned_first_elf = first_elf.partition('-')
        partitioned_second_elf = second_elf.partition('-')

        if int(partitioned_first_elf[0]) <= int(partitioned_second_elf[0]) and int(partitioned_first_elf[2]) >= int(partitioned_second_elf[2]):
            count += 1
        elif int(partitioned_first_elf[0]) >= int(partitioned_second_elf[0]) and int(partitioned_first_elf[2]) <= int(partitioned_second_elf[2]):
            count += 1
        #Part 2
        elif int(partitioned_first_elf[0]) <= int(partitioned_second_elf[0]) and int(partitioned_first_elf[2]) >= int(partitioned_second_elf[0]):
            count += 1
        elif int(partitioned_first_elf[0]) >= int(partitioned_second_elf[0]) and int(partitioned_first_elf[0]) <= int(partitioned_second_elf[2]):
            count += 1

print(count)

