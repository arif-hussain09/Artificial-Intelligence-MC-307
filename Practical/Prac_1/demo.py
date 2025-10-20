from inspect import stack
from collections import deque
class Node():
  def __init__(self,value):
    self.value=value
    self.children=[]
  def add_child(self,child_node):
    self.children.append(child_node)
  def __str__(self):
     return self.children
def DFS(node):
  if not node:
    return
  stack=[node]
  print(stack)
  while stack:
    node=stack.pop()
    print(node.value, end='->')
    stack.extend(reversed(node.children))

def BFS(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end='**')
        queue.extend(node.children)



def main():
  root = Node("A")
  root.children = [Node("B"), Node("C")]
  root.children[0].children = [Node("D")]
  root.children[1].children = [Node("E"),Node("F")]

  print(list(x) for x in list(root.__str__()))


  DFS(root)
  print()
  BFS(root)

if __name__ == "__main__":
  main()