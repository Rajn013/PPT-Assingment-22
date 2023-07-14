#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer 1:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertToDLL(root):
    if root is None:
        return None

    # Convert left subtree
    left_head = convertToDLL(root.left)

    # Convert current node
    if convertToDLL.prev is None:
        convertToDLL.head = root
    else:
        root.left = convertToDLL.prev
        convertToDLL.prev.right = root
    convertToDLL.prev = root

    # Convert right subtree
    convertToDLL(root.right)

    return convertToDLL.head

# Global variables for the head and previous nodes
convertToDLL.head = None
convertToDLL.prev = None

def printDLL(head):
    if head is None:
        return
    while head is not None:
        print(head.val, end=" ")
        head = head.right
    print()

# Example usage
root = TreeNode(25)
root.left = TreeNode(12)
root.right = TreeNode(30)
root.left.left = TreeNode(10)
root.left.right = TreeNode(36)
root.right.left = TreeNode(15)

# Convert binary tree to DLL
head = convertToDLL(root)

# Print the DLL
printDLL(head)


# In[2]:


#Answer 2:

def flipBinaryTree(root):
    if root is None:
        return None

    # If the node is a leaf, return itself
    if root.left is None and root.right is None:
        return root

    # Recursively flip the left and right subtrees
    flipped_left = flipBinaryTree(root.left)
    flipped_right = flipBinaryTree(root.right)

    # Swap the left and right children
    root.left = flipped_right
    root.right = flipped_left

    return root

def printTree(root):
    if root is None:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Flip the binary tree
flipped_tree = flipBinaryTree(root)

# Print the flipped tree
printTree(flipped_tree)


# In[3]:



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Flip the binary tree
flipped_tree = flipBinaryTree(root)

# Print the flipped tree
printTree(flipped_tree)


# In[4]:


#ANswer 3:

def printRootToLeafPaths(root):
    if root is None:
        return

    stack = [(root, str(root.val))]
    paths = []

    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            paths.append(path)

        if node.right is not None:
            stack.append((node.right, path + "->" + str(node.right.val)))

        if node.left is not None:
            stack.append((node.left, path + "->" + str(node.left.val)))

    for path in paths:
        print(path)


root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Print all root-to-leaf paths
printRootToLeafPaths(root)


# In[11]:


#Answer4:

def constructTree(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)

    root.left = constructTree(inorder[:root_index], preorder)
    root.right = constructTree(inorder[root_index+1:], preorder)

    return root

def isSameTree(inorder, preorder, postorder):
    tree1 = constructTree(inorder, preorder)
    tree2 = constructTree(inorder, postorder)

    return isSameTreeHelper(tree1, tree2)

def isSameTreeHelper(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False

    return (
        tree1.val == tree2.val and
        isSameTreeHelper(tree1.left, tree2.left) and
        isSameTreeHelper(tree1.right, tree2.right)
    )

# Example usage
inorder = [4, 2, 5, 1, 3]
preorder = [1, 2, 4, 5, 3]
postorder = [4, 5, 2, 3, 1]

result = isSameTree(inorder, preorder, postorder)

if result:
    print("Yes")
else:
    print("No")


# In[ ]:




