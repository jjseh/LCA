
# Lowest Common Ancestor
#
#
#           Binary Tree
#
#                 4
# 				  |
# 		  +-------+-------+
# 		  |				  |
# 		 10               7
# 		  |	              |
# 	  +---+---+       +---+---+
# 	  |       |       |       |
# 	  2       3       5       1
#   +-+-+   +-+-+   +-+-+   +-+-+
#   |   |   |   |   |   |   |   |
#   8   9   6   14  12  15  11  16
#


# A binary tree node
class Nodes:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root =  Nodes(4);
root.left = Nodes(10);
root.right = Nodes(7);
root.left.left = Nodes(2);
root.left.right = Nodes(3);
root.right.left = Nodes(5);
root.right.right = Nodes(1);
root.left.left.left = Nodes(8);
root.left.left.right = Nodes(9);
root.left.right.left = Nodes(6);
root.left.right.right = Nodes(14);
root.right.left.left = Nodes(12);
root.right.left.right = Nodes(15);
root.right.right.left = Nodes(11);
root.right.right.right = Nodes(16);


# Find Lowest Common Ancestor and return if both given nodes are found
# Return -1 if nodes not found
def findLowestCommonAncestor(root, node1, node2):
    # Store path from root to node1
    node1Path = []
    # Store path from root to node2
    node2Path = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findNodePath(root, node1Path, node1) or not findNodePath(root, node2Path, node2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while (i < len(node1Path) and i < len(node2Path)):
        if node1Path[i] != node2Path[i]:
            break
        i += 1
    return node1Path[i - 1]


#  Finds path between nodes
#  Store path in list path[]
#  If path exists return true, else if path does not exist return false
def findNodePath(root, path, k):
    # Base Case
    if root is None:
        return False

    # Store node
    # Remove node if not in path
    path.append(root.key)

    if root.key == k:
        return True

    # Check if node found in right or left subtree of tree
    if ((findNodePath(root.left, path, k) and root.left != None ) or
            (findNodePath(root.right, path, k) and root.right != None )):
        return True

    # Remove node if not found
    path.pop()
    return False


print("Lowest Common Ancestor of 8 and 9: = %d" %(findLowestCommonAncestor(root, 8, 9,)))
print("Lowest Common Ancestor of 7 and 5:= %d" %(findLowestCommonAncestor(root, 7, 5)))
print("Lowest Common Ancestor of 11 and 16: = %d" %(findLowestCommonAncestor(root, 11, 16)))
print("Lowest Common Ancestor of 10 and 7: = %d" %(findLowestCommonAncestor(root, 10, 7)))
print("Lowest Common Ancestor of 12 and 15: = %d" %(findLowestCommonAncestor(root, 12, 15)))