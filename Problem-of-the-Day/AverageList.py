# Python program to get average of a list
def average(array):
    res = [float(element) for element in array]
    return sum(res) / len(res)


# Driver Code
user_input = []
while True:
    input_to_console = input()
    if input_to_console == ".":
        break
    user_input.append(input_to_console)

average = average(user_input)

# Printing average of the list
print(average)
