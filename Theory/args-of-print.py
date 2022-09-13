print('Chip', 'Dale', sep='&')  # Chip&Dale
# print('Chip', 'Dale', sep=0)    # TypeError: sep must be None or a string, not int

print('Gadget', 'Hackwrench', sep=' ')
# Gadget Hackwrench

print('Gadget', 'Hackwrench')
# Gadget Hackwrench

print(13, 'th', sep='')  # 13th

print('Monterey')
print()
print('Jack')

print('Tick-Tock', end=' the ')
print('Crocodil', end='e\n\n')
# Tick-Tock the Crocodile

characters = ['Humphrey the Bear', 'Spike the Bee', 'Fat Cat']
print(*characters)

# Letter-spacing
# print(*input(), sep=' ' * int(input()))

line1 = "Night, square, apothecary, lantern,"
line2 = "Its meaningless and pallid light."
line3 = "Return a half a lifetime after – "
line4 = "All will remain. A scapeless rite."

# your one print() statement here
print(line1, line2, line3, line4, sep="\n")

adj = "Good"
part_of_day = "morning"
comma = ","
title = "Ms."
surname = "Johnson"

# your print() function
print(adj, part_of_day + comma, title, surname, end="!")

numbers = [int(x) for x in input().split()]
# print all numbers without spaces
print(*numbers, sep="")


