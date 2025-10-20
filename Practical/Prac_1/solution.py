import copy
class Node():
    def __init__(self,state,action,parent):
        self.state=state
        self.action=action
        self.parent=parent

# Stack frontier

class StackFrontier():
    def __init__(self):
        self.frontier=[]
    
    def add(self,node):
        self.frontier.append(node)
    
    
    def contain_state(self,state):
        return any(node.state==state for node in self.frontier)
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Frontier is empty")
        return self.frontier.pop()
    
    def isEmpty(self):
        return len(self.frontier)==0

# Queue Frontier

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.isEmpty():
            raise Exception("Frontier is empty")
        return self.frontier.pop(0) # <- FIFO
    
def get_neighbors(puzzle):
    nbd=[]
    n = len(puzzle)
    m = len(puzzle[0])

    row , col= None , None # index of blank space
    # finding the empty place index
    for i in range(n):
        for j in range(m):
            if puzzle[i][j]==0:
                row , col = i , j
        
    moves=[(1,0),(0,1),(-1,0),(0,-1)]

    for dr , dc in moves:
        nr , nc = row +dr , col+dc 
        if 0<=nr < n and 0 <= nc<m:
            newpuzzle=copy.deepcopy(puzzle)
            # swaping the tile
            newpuzzle[row][col] , newpuzzle[nr][nc] = newpuzzle[nr][nc],newpuzzle[row][col]
            nbd.append(newpuzzle) 
    return nbd   
def print_solution(node):
    path=[]
    while node is not None:
        path.append(node.state)
        node=node.parent
    
    path.reverse()

    print("------:Solution:------")
    for state in path:
        for row in state:
            print(row)
        print()
        
def main():
    start_state = [
        [1, 2, 3],
        [4, 8, 6],
        [7, 5, 0]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 6, 8]
    ]
    startNode=Node(state=start_state,parent=None,action=None)
    frontier=QueueFrontier()
    visited=set()
    frontier.add(startNode)

    while not frontier.isEmpty():
        node=frontier.remove()

        if node.state==goal_state:
            print_solution(node)
            return True
        visited.add(tuple(map(tuple,node.state)))

        for nieghbor in get_neighbors(node.state):
            if tuple(map(tuple,nieghbor)) not in visited and not  frontier.contain_state(nieghbor):
                child=Node(state=nieghbor,parent=node,action=None)
                frontier.add(child)
    print("No solution found.")
    return False

if __name__=="__main__":
    main()