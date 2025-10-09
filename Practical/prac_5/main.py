import random
from typing import List, Tuple

# --------------------------------------------------------------------------
# 1. HELPER FUNCTIONS for PARSING and EVALUATION
# --------------------------------------------------------------------------

def parse_dimacs_from_string(dimacs_string: str) -> Tuple[List[Tuple[int, ...]], int]:
    """
    Parses a 3-SAT problem from a string in standard DIMACS CNF format.
    
    A formula is a list of clauses. A clause is a tuple of literals (integers).
    Example: (x1 or ~x2 or x3) is represented as (1, -2, 3)

    Returns:
        - The formula as a list of clauses.
        - The total number of variables.
    """
    lines = dimacs_string.strip().split('\n')
    formula = []
    num_variables = 0
    
    for line in lines:
        line = line.strip()
        # Skip comments ('c') and empty lines
        if not line or line.startswith('c'):
            continue
        # The problem definition line ('p cnf num_vars num_clauses')
        if line.startswith('p cnf'):
            parts = line.split()
            num_variables = int(parts[2])
        # A line with literals for a clause
        else:
            # Clause lines end with a 0, which we remove
            literals = tuple(map(int, line.split()[:-1]))
            formula.append(literals)
            
    return formula, num_variables

def generate_random_assignment(num_variables: int) -> List[bool]:
    """Generates a random truth assignment (a list of booleans)."""
    return [random.choice([True, False]) for _ in range(num_variables)]

def calculate_score(formula: List[Tuple[int, ...]], assignment: List[bool]) -> int:
    """
    This is our Objective Function. It calculates how many clauses are satisfied
    by the given assignment.
    """
    satisfied_count = 0
    for clause in formula:
        is_clause_satisfied = False
        for literal in clause:
            # Convert 1-indexed variable to 0-indexed list index
            variable_index = abs(literal) - 1
            
            # Check if the literal's value is True under the assignment
            if (literal > 0 and assignment[variable_index] is True) or \
               (literal < 0 and assignment[variable_index] is False):
                is_clause_satisfied = True
                break  # One true literal is enough to satisfy the clause
        
        if is_clause_satisfied:
            satisfied_count += 1
    return satisfied_count

# --------------------------------------------------------------------------
# 2. THE STOCHASTIC HILL CLIMBING ALGORITHM
# --------------------------------------------------------------------------

def stochastic_hill_climbing(formula: List[Tuple[int, ...]], num_variables: int, max_iterations: int = 1000):
    """
    Attempts to find a satisfying assignment for a 3-SAT formula.
    """
    total_clauses = len(formula)
    
    # Step 1: Initialization
    current_assignment = generate_random_assignment(num_variables)
    current_score = calculate_score(formula, current_assignment)
    
    print("🚀 Starting Stochastic Hill Climbing...")
    print(f"Initial Score: {current_score} / {total_clauses}")

    for i in range(max_iterations):
        # Check if we have found a solution
        if current_score == total_clauses:
            print(f"\n✅ Solution found at iteration {i}!")
            return current_assignment, current_score, True

        # Step 2: Deterministic Filtering - Find all better neighbors
        uphill_moves = [] # Will store tuples of (index_to_flip, resulting_score)
        
        for var_idx_to_flip in range(num_variables):
            # Create a temporary neighbor assignment by flipping one variable
            neighbor_assignment = list(current_assignment)
            neighbor_assignment[var_idx_to_flip] = not neighbor_assignment[var_idx_to_flip]
            
            neighbor_score = calculate_score(formula, neighbor_assignment)
            
            # If the neighbor is strictly better, add it to our list of candidates
            if neighbor_score > current_score:
                uphill_moves.append((var_idx_to_flip, neighbor_score))

        # Step 3: Probabilistic Selection
        if not uphill_moves:
            # If no better neighbors exist, we are at a local maximum
            print(f"\n⚠️ Stuck at a local maximum at iteration {i}. No uphill moves available.")
            return current_assignment, current_score, False
            
        # Randomly choose one of the good moves
        chosen_idx, new_score = random.choice(uphill_moves)
        
        # Apply the chosen move to our current state
        current_assignment[chosen_idx] = not current_assignment[chosen_idx]
        current_score = new_score
        
        if (i + 1) % 50 == 0:
            print(f"  Iteration {i+1:4d}: Current Score = {current_score}")

    print(f"\n❌ Reached max iterations ({max_iterations}) without finding a solution.")
    return current_assignment, current_score, False

# --------------------------------------------------------------------------
# 3. MAIN EXECUTION BLOCK
# --------------------------------------------------------------------------

if __name__ == "__main__":
    # A sample 3-SAT problem in DIMACS format.
    # This formula is satisfiable. One solution is [F, T, T, F]
    # (x1=False, x2=True, x3=True, x4=False)
    dimacs_problem = """
    c A sample satisfiable 3-CNF formula.
    p cnf 4 5
    -1 2 3 0
    1 -2 -3 0
    1 2 -4 0
    1 -3 4 0
    -2 -3 -4 0
    """
    
    # Parse the problem from the string
    formula, num_variables = parse_dimacs_from_string(dimacs_problem)
    total_clauses = len(formula)
    
    print("-" * 40)
    print(f"Problem Loaded: {num_variables} variables, {total_clauses} clauses.")
    print("-" * 40)
    
    # Run the algorithm
    best_assignment, best_score, found_solution = stochastic_hill_climbing(
        formula=formula, 
        num_variables=num_variables, 
        max_iterations=1000
    )
    
    # --- Print Final Results ---
    print("-" * 40)
    print("Algorithm Finished.")
    print(f"Solution Found: {'Yes!' if found_solution else 'No.'}")
    print(f"Final Best Score: {best_score} out of {total_clauses} clauses satisfied.")
    
    # Print the assignment in a readable format (e.g., x1=True, x2=False)
    readable_assignment = [f"x{i+1}={val}" for i, val in enumerate(best_assignment)]
    print(f"Best Assignment Found: {', '.join(readable_assignment)}")
    print("-" * 40)