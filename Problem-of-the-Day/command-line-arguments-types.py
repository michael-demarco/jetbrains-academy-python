import sys

args = sys.argv

# further code of the script "add_four_numbers.py"
answer_list = [int(i) for i in args if i.isdigit()]

print(sum(answer_list))
