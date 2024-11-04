# Original list of points in (x, y) format

# Function to convert each (x, y) to chess notation
def convert_to_chess_notation(points):
    converted_points = []
    for x, y in points:
        # Convert x to the appropriate letter (a-f)
        letter = chr(ord('a') + y)
        # Convert y to the appropriate row (1-6, from bottom to top)
        row = 6 - x
        # Combine letter and row into chess notation and add to list
        converted_points.append(f"{letter}{row}")
    return converted_points

# Convert the points and print
print(convert_to_chess_notation([(0, 0), (2, 1), (3, 3), (1, 2), (3, 1), (4, 3), (5, 1), (3, 2), (1, 3), (3, 4), (5, 5)]))
print(convert_to_chess_notation([(5, 0), (3, 1), (4, 3), (2, 2), (1, 0), (0, 2), (2, 1), (3, 3), (4, 5), (2, 4), (0, 5)]))


# a6,b4,d3,c5,b3,d2,b1,c3,d5,e3,f1
# a1,b3,d2,c4,a5,c6,b4,d3,f2,e4,f6
