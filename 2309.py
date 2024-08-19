Dwarf = []

for _ in range(9):
    Dwarf.append(int(input()))

Dwarf_temp = Dwarf[:]

for i in range(9):
    for k in range(i + 1,9):
        del Dwarf_temp[k]
        del Dwarf_temp[i]
        if(sum(Dwarf_temp) == 100):
            Dwarf_temp.sort()
            for i in Dwarf_temp:
                print(i)
            exit(0)
        else:
            Dwarf_temp = Dwarf[:]
