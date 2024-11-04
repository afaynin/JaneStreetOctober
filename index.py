# import sys
class Movement:
    def __init__(self):
        self.paths = []  # Store all successful paths
        # self.active_calls = 0

    def legal_move(self, position: tuple, previous_moves: list):
        # Check if the move has already been made or is out of bounds
        if position in previous_moves:
            return False
        if 0 <= position[0] < 6 and 0 <= position[1] < 6: 
            return True
        return False

    def knight_move(self, position: tuple, goal: tuple, previous_moves: list):
        # self.active_calls += 1
        # sys.stdout.write(f"\rActive calls: {self.active_calls}")
        # sys.stdout.flush()

        # Check if the goal is reached
        if position == goal: 
            self.paths.append(previous_moves)  # Add the successful path
            return
        if len(previous_moves) > 12:
            # self.active_calls -= 1 
            return
        # Define possible knight moves
        moves = [
            (position[0] + 2, position[1] + 1),
            (position[0] + 1, position[1] + 2),
            (position[0] - 2, position[1] - 1),
            (position[0] - 1, position[1] - 2),
            (position[0] - 2, position[1] + 1),
            (position[0] + 2, position[1] - 1),
            (position[0] - 1, position[1] + 2),
            (position[0] + 1, position[1] - 2),
        ]

        # Recursively try each legal move
        for pos in moves:
            if self.legal_move(pos, previous_moves): 
                # Pass a new list for each recursive call to keep paths independent
                self.knight_move(pos, goal, previous_moves + [pos])

# Usage
movement = Movement()
movement.knight_move((0, 0), (5, 5), [(0, 0)])
movement.knight_move((5, 0), (0, 5), [(5, 0)])
# Print all unique paths found
for path in movement.paths:
    print(path)
