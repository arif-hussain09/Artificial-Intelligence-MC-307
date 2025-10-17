import random

def evaluate_clauses(clauses, assignment):
    """
    Calculates how many clauses in the formula are satisfied by the given assignment.

    Args:
        clauses (list of lists of int): The 3-SAT formula. Each inner list is a clause.
                                       A positive int represents a variable, negative is its negation.
                                       Example: [[1, -2, 3], [-1, 2, -4]]
        assignment (dict): A mapping from variable (int) to its boolean value (True/False).
                           Example: {1: True, 2: False, 3: True, 4: False}

    Returns:
        int: The number of satisfied clauses.
    """
    num_satisfied = 0
    for clause in clauses:
        is_clause_satisfied = False
        for literal in clause:
            variable = abs(literal)
            is_negated = literal < 0
            
            # Check if the literal's value makes the clause true
            if (is_negated and not assignment[variable]) or \
               (not is_negated and assignment[variable]):
                is_clause_satisfied = True
                break  # Move to the next clause once one true literal is found
        
        if is_clause_satisfied:
            num_satisfied += 1
            
    return num_satisfied

def stochastic_hill_climbing(clauses, num_variables, max_restarts=10, max_steps=1000):
    """
    Attempts to solve a 3-SAT problem using Stochastic Hill Climbing with random restarts.

    Args:
        clauses (list of lists of int): The 3-SAT formula.
        num_variables (int): The total number of unique variables in the formula.
        max_restarts (int): The maximum number of times to restart from a random assignment.
        max_steps (int): The maximum number of steps to take in each climbing attempt.

    Returns:
        dict or None: A satisfying assignment (dict) if one is found, otherwise None.
    """
    total_clauses = len(clauses)
    
    for restart in range(max_restarts):
        # 1. Start with a random assignment
        current_assignment = {i: random.choice([True, False]) for i in range(1, num_variables + 1)}
        
        print(f"\n--- Restart #{restart + 1} ---")
        
        for step in range(max_steps):
            current_score = evaluate_clauses(clauses, current_assignment)
            print(f"Step {step}: Score = {current_score}/{total_clauses}")

            # 2. Check if we found a solution
            if current_score == total_clauses:
                print("\nSolution found!")
                return current_assignment
            
            # 3. Find all "uphill" neighbors
            uphill_neighbors = []
            for var_to_flip in range(1, num_variables + 1):
                # Create a temporary neighbor assignment by flipping one variable
                neighbor_assignment = current_assignment.copy()
                neighbor_assignment[var_to_flip] = not neighbor_assignment[var_to_flip]
                
                neighbor_score = evaluate_clauses(clauses, neighbor_assignment)
                
                if neighbor_score > current_score:
                    uphill_neighbors.append((neighbor_assignment, neighbor_score))

            # 4. Check if we are at a local maximum
            if not uphill_neighbors:
                print("Stuck at a local maximum or plateau. Restarting...")
                break # Break inner loop to trigger a restart
            
            # 5. Stochastic step: randomly choose one of the better neighbors
            best_neighbor, _ = random.choice(uphill_neighbors)
            current_assignment = best_neighbor
            
    print("\nFailed to find a solution after all restarts.")
    return None

# --- Example Usage ---
if __name__ == "__main__":
    # A satisfiable 3-SAT problem instance
    # Formula: (x1 ∨ ¬x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ ¬x4) ∧ (x3 ∨ x4 ∨ x1) ∧ (¬x2 ∨ ¬x3 ∨ x4)
    # One known solution: {1: True, 2: True, 3: False, 4: True}
    
    problem_clauses = [
        [1, -2, 3],
        [-1, 2, -4],
        [3, 4, 1],
        [-2, -3, 4]
    ]
    problem_num_variables = 4
    
    print("Attempting to solve the 3-SAT problem...")
    solution = stochastic_hill_climbing(
        clauses=problem_clauses,
        num_variables=problem_num_variables,
        max_restarts=20, # More restarts give a higher chance of success
        max_steps=100
    )
    
    if solution:
        print("\nSatisfying Assignment:")
        # Sort by variable number for clean output
        for var in sorted(solution.keys()):
            print(f"  Variable {var}: {solution[var]}")
    else:
        print("\nNo solution was found for the given problem.")