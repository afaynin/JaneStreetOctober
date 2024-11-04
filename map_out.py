import sys
import ast

# Initialize an empty list to store all lists of tuples
all_lists = []
for line in sys.stdin:
    try:
        all_lists.append(ast.literal_eval(line.strip()))
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing line: {line}. Error: {e}")
        continue   
# Read each line from stdin
# for line in sys.stdin:
#     # Remove any trailing whitespace and parse the line as a Python literal
#     try:
#         tuple_list = ast.literal_eval(line.strip())
#         # Ensure that it parsed into a list of tuples
#         if isinstance(tuple_list, list) and all(isinstance(t, tuple) for t in tuple_list):
#             all_lists.append(tuple_list)
#         else:
#             print(f"Warning: Line '{line.strip()}' is not in the expected format.")
#     except (SyntaxError, ValueError):
#         print(f"Error: Could not parse line '{line.strip()}'.")

# Output the parsed data
# print("Parsed lists of tuples:")
A = 3
B = 4
C = 5
Map = [
[A,B,B,C,C,C],
[A,B,B,C,C,C],
[A,A,B,B,C,C],
[A,A,B,B,C,C],
[A,A,A,B,B,C],
[A,A,A,B,B,C],
]
move_sets1= []
move_set_positions1 = []
move_sets2= []
move_set_positions2 = []
num = 0
for lst in all_lists:
    num += 1
    temp = []
    for val in lst:
        if Map[val[0]][val[1]] == A:
            temp.append("A")
        if Map[val[0]][val[1]] == B:
            temp.append("B")
        if Map[val[0]][val[1]] == C:
            temp.append("C")
    if int(len(all_lists)/2) >=  num:
        move_sets1.append(temp)
        move_set_positions1.append(lst)
    else:
        move_sets2.append(temp)
        move_set_positions2.append(lst)
same_move_set = []
same_move_set_pos = []
for index, lst in enumerate(move_sets1):
    for index2, lst2 in enumerate(move_sets2):
        if lst == lst2:
            if lst not in same_move_set:
                same_move_set_pos.append((move_set_positions1[index], move_set_positions2[index2]))

                same_move_set.append(lst)
# for lst in move_set_positions1:
#     for lst2 in move_set_positions2:
#         # print(lst)
#         if lst == lst2:
#             print(lst)
#             if lst not in same_move_set_pos:
#                 same_move_set_pos.append(lst)
# print(move_sets1)
# print(move_sets2)
print(same_move_set)
print(same_move_set_pos)
