import random
import sys
import ast

# Initialize an empty list to store all lists of tuples
# Input =ast.literal_eval(sys.stdin.read()) 
input_lines = sys.stdin.read().strip().splitlines()

# Parse each line separately
parsed_data = [ast.literal_eval(line) for line in input_lines]


same_move_set, same_move_set_pos = parsed_data
# print(same_move_set)
# print(same_move_set_pos)
values = {
    'A' : 3,
    'B' : 4,
    'C' : 8,
    }
def calculate_score(move_set, values):

    score = 0
    for index, val in enumerate(move_set):
        if index == 0:
            score = values[val]
        else:
            if move_set[index - 1] is val:
                score += values[val]
            else:
                score *= values[val]
    return score
# print(same_move_set)
for thing in range(2500):
    values = {
            'A' : int(random.random() * 3) + 1,
            'B' : int(random.random() * 3) + 1,
            'C' : int(random.random() * 4)+ 1,
    
            }
    for num in range(len(same_move_set)):
        # print(calculate_score(same_move_set[num], values))
        if calculate_score(same_move_set[num], values) == 2024:
            print(f"{values}, {same_move_set[num]}, {same_move_set_pos[num]}")
