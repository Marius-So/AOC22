#! python
with open('01a.txt', 'r') as inp:
    lines = inp.readlines()
    lines = [e[:-1] for e in lines] + ['']

elf_proviants = []
new_elf = 0
for line in lines:
    if line != '':
        new_elf += int(line)
    else:
        elf_proviants.append(new_elf)
        new_elf = 0

print('part one: ', max(elf_proviants))

print('part two: ', sum(sorted(elf_proviants)[-3:]))
