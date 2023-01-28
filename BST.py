# BST: Binary Search Tree.  Data Structure = binary tree
# binary tree nodes have a max of two children nodes.
# child nodes are 'left' or 'right'

# Part 1: Create a BSTNode class

class BSTNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

  def __repr__(self):
    return str(self.data)

# test data


node1 = BSTNode(3)
print(node1)  # displays 3

node2 = BSTNode(4, left=node1)
print(node2)  # displays 4

node3 = BSTNode()
print(node3)  # displays None

node3.data = 5
print(node3)  # displays 5


# Parts 2 & 3: Create a BST class and add functionality

class root:
  def __init__(self, root=None):
    self.root = root
    self.contents = []

  def __str__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output

  def __repr__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output

  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)
  
  def add(self,node):
    #data wrong type
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("You must pass an int or a BSTNode")

    #data int, make new BSTNode
    if type(node) == int:
      node = BSTNode(node)

    #node already in tree
    if node.data in self.contents:
      return

    #tree empty
    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return

    #call new (recursive) function; don't need to check other conditions again
    self.add_node(self.root, node)

  def add_node(self, cur_node, new_node):
    # New node bigger - go right
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.contents.append(new_node.data)
        return
      else:
        #recurse/traverse
        self.add_node(cur_node.right, new_node)
    else: #new node smaller, go left
      if cur_node.left == None:
        cur_node.left = new_node
        self.contents.append(new_node.data)
        return
      else:
        #recurse/traverse
        self.add_node(cur_node.left, new_node)

