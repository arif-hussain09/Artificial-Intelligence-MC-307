import heapq

class PuzzleNode:
    """A class to represent a state in the 8-puzzle search tree."""
    def __init__(self, state, parent=None, move=None, g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g  # Cost from start to current node
        self.h = self.calculate_manhattan_distance() # Heuristic cost to goal
        self.f = self.g + self.h # Total estimated cost

    def __lt__(self, other):
        """Comparator for the priority queue."""
        return self.f < other.f

    def calculate_manhattan_distance(self):
        """
        Calculates the Manhattan distance heuristic for the current state.
        The distance is the sum of the Manhattan distances of each tile 
        from its goal position.
        """
        distance = 0
        goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        for r in range(3):
            for c in range(3):
                tile = self.state[r][c]
                if tile != 0:
                    # Find the goal position of the tile
                    goal_r, goal_c = -1, -1
                    for gr in range(3):
                        for gc in range(3):
                            if goal_state[gr][gc] == tile:
                                goal_r, goal_c = gr, gc
                                break
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def get_neighbors(self):
        """Generates all valid neighbor states from the current state."""
        neighbors = []
        # Find the position of the empty tile (0)
        empty_r, empty_c = -1, -1
        for r in range(3):
            for c in range(3):
                if self.state[r][c] == 0:
                    empty_r, empty_c = r, c
                    break
        
        # Possible moves: up, down, left, right
        moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        for move_name, (dr, dc) in moves.items():
            new_r, new_c = empty_r + dr, empty_c + dc
            
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                # Create a new state by swapping the empty tile
                new_state_list = [list(row) for row in self.state]
                new_state_list[empty_r][empty_c], new_state_list[new_r][new_c] = \
                    new_state_list[new_r][new_c], new_state_list[empty_r][empty_c]
                
                # Convert back to tuple of tuples to be hashable
                new_state = tuple(tuple(row) for row in new_state_list)
                neighbors.append(PuzzleNode(new_state, self, move_name, self.g + 1))
                
        return neighbors

def solve_8_puzzle(initial_state):
    """
    Solves the 8-puzzle problem using the A* search algorithm.
    
    Args:
        initial_state (tuple of tuples): The starting configuration of the puzzle.

    Returns:
        list of str or None: A list of moves to solve the puzzle, or None if unsolvable.
    """
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    
    # The open list is a priority queue of nodes to visit
    open_list = []
    # The closed set stores states that have already been visited
    closed_set = set()

    start_node = PuzzleNode(initial_state)
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f-score
        current_node = heapq.heappop(open_list)
        
        # If we reached the goal, reconstruct and return the path
        if current_node.state == goal_state:
            path = []
            node = current_node
            while node.parent is not None:
                path.append(node.move)
                node = node.parent
            return path[::-1] # Reverse to get path from start to goal

        closed_set.add(current_node.state)

        for neighbor in current_node.get_neighbors():
            if neighbor.state in closed_set:
                continue

            # Check if neighbor is in the open list with a higher f-score
            in_open_list = False
            for i, item in enumerate(open_list):
                if item.state == neighbor.state:
                    in_open_list = True
                    if neighbor.g < item.g:
                        # If we found a better path, update the node
                        open_list[i] = neighbor
                        heapq.heapify(open_list)
                    break
            
            if not in_open_list:
                heapq.heappush(open_list, neighbor)

    return None # No solution found

def print_board(state):
    """Prints the puzzle board in a readable format."""
    for row in state:
        print(" ".join(str(tile) if tile != 0 else '_' for tile in row))
    print()

# --- Example Usage ---
if __name__ == "__main__":
    # A moderately difficult, solvable initial state
    initial_state_tuple = ((7, 2, 4), (5, 0, 6), (8, 3, 1))
    
    print("Initial State:")
    print_board(initial_state_tuple)
    
    solution_path = solve_8_puzzle(initial_state_tuple)
    
    if solution_path:
        print(f"Solution found in {len(solution_path)} moves!")
        print("Path:", " -> ".join(solution_path))

        # Optional: Print the states along the solution path
        current_state = [list(row) for row in initial_state_tuple]
        for move in solution_path:
            er, ec = -1, -1
            for r in range(3):
                for c in range(3):
                    if current_state[r][c] == 0:
                        er, ec = r, c
            
            if move == 'U': nr, nc = er - 1, ec
            elif move == 'D': nr, nc = er + 1, ec
            elif move == 'L': nr, nc = er, ec - 1
            elif move == 'R': nr, nc = er, ec + 1

            current_state[er][ec], current_state[nr][nc] = current_state[nr][nc], current_state[er][ec]
            print(f"\nMove: {move}")
            print_board(tuple(tuple(row) for row in current_state))
            
    else:
        print("No solution found. The puzzle might be unsolvable.")
