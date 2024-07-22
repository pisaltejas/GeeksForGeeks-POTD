#User function Template for python3
class Solution:
    def largestBst(self, root):
        # code edutechbarsha
        # Helper function to perform the necessary checks and return relevant info
        def helper(node):
             # Base case: empty subtree
            if not node:
               return True,0,float('inf'),float('-inf'),0
       
            
            # Recursively get info from left and right subtrees
            l_is_bst,l_size,l_min,l_max,l_largest_bst = helper(node.left)
            r_is_bst,r_size,r_min,r_max,r_largest_bst = helper(node.right)
            
            # Check if current node is BST
            if l_is_bst and r_is_bst and l_max < node.data < r_min:
                # Current node is BST
                size = l_size + r_size + 1
                return True,size,min(node.data, l_min), max(node.data, r_max),max(size,l_largest_bst,r_largest_bst)
            else:    
                # Current node is not BST
                return False,0,0,0, max(l_largest_bst, r_largest_bst)
                
        
        # Get the result from the helper function
        _,_,_,_, largest_bst_size = helper(root)
        return largest_bst_size

#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1

        # Move to the next element
        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1

        # Move to the next element
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.largestBst(root)
        print(result)

# } Driver Code Ends
