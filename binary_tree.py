
class TreeNode: 

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):

        if self.root == None:
            self.root = TreeNode(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):

        if key < node.key:
            if node.left == None: #see if there is an opening to the left
                node.left = TreeNode(key) #take the opening
            else:
                self.insert_recursive(node.left, key) #spot taken, compare key to that node
            
        elif key > node.key:
            if node.right == None: #check if there is an opening to the right
                node.right = TreeNode(key) #take the opening
            else: #no opening
                self.insert_recursive(node.right, key) #compare right node with our key

    def print_tree(self):
        self.print_recursive(self.root, 0)

    def print_recursive(self, node, depth):

        if node is None: #base case
            return None
        
        self.print_recursive(node.right, depth + 1)
        print("    "* depth + str(node.key))
        self.print_recursive(node.left, depth + 1)


    def search(self, key):
        return self.search_recursive(self.root, key)
    
    def search_recursive(self, node, key):

        if node == None: #Negative Base Case, Target not Here
            return False
        
        if node.key == key: #Positive Base Case, Target found
            return True
        elif key < node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)
        
    def find_smallest(self, node): #will take in the right node of the node we want to remove

        while node.left: #if there is a left node
            node = node.left #replace current with left node
        return node

        
    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):

        if node == None: #Base case: what we are trying to remove doesn't exist here
            return node
        
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
        else: #I've found wat I need to remove
            if node.left == None: #I either have a single branch right, or this node is a leaf
                return node.right
            elif node.right == None: #I know I have a single left branch
                return node.left
            
            #If I make it here I know I have a double branch
            #find the smallest node to my right
            smallest = self.find_smallest(node.right)
            #use that nodes value to replace this nodes value (remove target)
            node.key = smallest.key
            # go back and remove the smallest value
            node.right = self.delete_recursive(node.right, smallest.key)
        return node
    
    def in_order_traverse(self):
        self.in_order_traverse_recursive(self.root)

    def in_order_traverse_recursive(self, node):

        if node:
            self.in_order_traverse_recursive(node.left)
            print(node.key)
            self.in_order_traverse_recursive(node.right)






tree = BinaryTree()
nodes = [50,30,20,40,70,60,80,90]
 
for node in nodes: #populating tree
    tree.insert(node)


tree.print_tree() #printing my tree
print("~"*50)
tree.delete(70)
tree.print_tree() #printing my tree

tree.in_order_traverse()
