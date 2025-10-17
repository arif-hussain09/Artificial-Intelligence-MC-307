class Node:
    """Represents a node in the AND-OR graph."""
    def __init__(self, name, h_cost, is_solved=False):
        self.name = name
        self.h_cost = h_cost
        self.is_solved = is_solved
        self.parent = None
        self.children = []

def ao_star_search(graph, heuristics, start_node_name):
    """
    Implements the AO* search algorithm to find the minimum cost solution graph.

    Args:
        graph (dict): The AND-OR graph structure. 
                      Format: {'Node': [[('Child1', cost1), ('Child2', cost2)], [('Child3', cost3)]]}
                      Inner lists represent AND conditions, outer list represents OR conditions.
        heuristics (dict): A dictionary of heuristic costs for each node.
        start_node_name (str): The name of the starting node.

    Returns:
        tuple or (None, None): A tuple containing the solution path and its cost,
                               or (None, None) if no solution is found.
    """
    
    # Store computed costs and the solution graph
    computed_costs = {}
    solution_graph = {}
    
    def get_h_cost(node_name):
        return heuristics.get(node_name, float('inf'))

    def get_computed_cost(node_name):
        return computed_costs.get(node_name, float('inf'))

    def set_computed_cost(node_name, cost):
        computed_costs[node_name] = cost

    def get_min_cost_child_nodes(node_name):
        """Finds the child/children with the minimum cost for a given OR node."""
        min_cost = float('inf')
        min_cost_nodes = []
        
        # graph[node_name] contains list of AND-connected node groups
        for and_group in graph.get(node_name, []):
            cost = 0
            nodes = []
            for child_name, weight in and_group:
                cost += get_computed_cost(child_name) + weight
                nodes.append(child_name)

            if cost < min_cost:
                min_cost = cost
                min_cost_nodes = nodes
        
        return min_cost, min_cost_nodes

    def ao_star_recursive(node_name):
        """The recursive part of the AO* algorithm."""
        print(f"Expanding node: {node_name}")

        # Base case: if node is terminal (no children in graph), cost is its heuristic
        if node_name not in graph:
            set_computed_cost(node_name, get_h_cost(node_name))
            return
        
        # This is an OR node, we need to find the minimum cost path
        min_cost = float('inf')
        min_cost_nodes = []

        # Iterate over all AND-connected groups of children
        for and_group in graph.get(node_name, []):
            current_cost = 0
            
            # Recursively call ao_star for each child in the AND group
            for child_name, weight in and_group:
                if child_name not in computed_costs:
                    ao_star_recursive(child_name)
                current_cost += get_computed_cost(child_name) + weight

            if current_cost < min_cost:
                min_cost = current_cost
                min_cost_nodes = [child for child, weight in and_group]
        
        # Update the cost and solution path for the current node
        set_computed_cost(node_name, min_cost)
        solution_graph[node_name] = min_cost_nodes


    # --- Main execution starts here ---
    print("Starting AO* Search...")
    ao_star_recursive(start_node_name)
    
    # Reconstruct the final solution path from the solution_graph
    solution_path = []
    
    def reconstruct_path(node_name):
        solution_path.append(node_name)
        if node_name in solution_graph and solution_graph[node_name]:
            for child_node in solution_graph[node_name]:
                 # Only branch if the child is not a leaf in the solution path
                if child_node in solution_graph:
                    reconstruct_path(child_node)
    
    reconstruct_path(start_node_name)
    
    final_cost = get_computed_cost(start_node_name)
    
    if final_cost == float('inf'):
        return None, None
        
    return solution_path, final_cost


# --- Example Usage ---
if __name__ == "__main__":
    # Heuristic values for each node
    heuristics_map = {
        'A': 5, 'B': 7, 'C': 8, 'D': 4, 'E': 6, 'F': 5,
        'G': 3, 'H': 2, 'I': 0, 'J': 0
    }

    # The AND-OR graph structure
    # A can be solved by B, OR by C and D (AND)
    # B can be solved by E or F
    # C can be solved by G or H
    # D can be solved by I or J
    graph_structure = {
        'A': [[('B', 1)], [('C', 1), ('D', 1)]],
        'B': [[('E', 1)], [('F', 1)]],
        'C': [[('G', 1)], [('H', 1)]],
        'D': [[('I', 1)], [('J', 1)]]
    }
    
    start_node = 'A'
    
    path, cost = ao_star_search(graph_structure, heuristics_map, start_node)
    
    if path:
        print(f"\nSolution found with cost: {cost}")
        print("Path from start to goal:")
        print(" -> ".join(path))
        # For a more detailed view of the final solution graph
        # print("\nFinal Solution Graph Pointers:")
        # print(solution_graph) 
    else:
        print("\nNo solution found.")
