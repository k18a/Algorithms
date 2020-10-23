# define tree node
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    # string method for tree node
    def __str__(self):
        return str(self.info) 

# define binary search tree
class BinarySearchTree:
    # initialize binary search tree
    def __init__(self): 
        self.root = None

    # insert value into binary search tree
    def create(self, val):  
        # if root is none
        if self.root == None:
            # add to root node
            self.root = Node(val)
        # if root is note None
        else:
            # initialize current node
            current = self.root
            # traverse through tree
            while True:
                # if value is less than current value
                if val < current.info:
                    # if left node exists
                    if current.left:
                        # reinitialize current node
                        current = current.left
                    # if not
                    else:
                        # add value to left node
                        current.left = Node(val)
                        # break loop after adding
                        break
                # if value is greater than current value
                elif val > current.info:
                    # if right node exists
                    if current.right:
                        # reinitialize current value
                        current = current.right
                    # if not
                    else:
                        # add value to right node
                        current.right = Node(val)
                        # break after adding
                        break
                # if value is equal to current node
                else:
                    # break without adding duplicates
                    break

# function to get height of tree
def height(root):
    # define base case
    # if root does not exist
    if root == None:
        # return one less value
        return -1
    else:
        # recursively get height of left node
        left_height = height(root.left)
        # recursively get height of right node
        right_height = height(root.right)
        # return max value of left and right and current node
        return 1 + max(left_height, right_height)


if __name__ == "__main__":
    tree = BinarySearchTree()
    arr = [1,2,3,4]
    for value in arr:
        tree.create(value)
    print(height(tree.root))
