







# Write a program that reads a sequence of numbers from the first line and the number x from the second line.
# Then it should output all positions of x in the numerical sequence.
# The position count starts from 0.
# In case x is not in the sequence, print the line "not found" (quotes omitted, lowercased).
# Positions should be displayed in one line, in ascending order of the value.
# Hint
# Here is a brief outline:
#   read the input, then
#   create a new list for the positions and, when iterating over the list of numbers,
#   append all the indices of the found occurrences of x to that list (e.g. you can use a counter variable to find them).
#   Finally, join the list of indexes or print the message "not found".

# put your python code here

# put your python code here


x = input()
y = input()

result = []

list_without_spaces = x.split(" ")  # list
for i in enumerate(list_without_spaces):
    if str(list_without_spaces.__getattribute__(i)) == y:
        result.append(i)

if result:
    for ele in result:
        print(ele,end = " ")
else:
    print("not found")

