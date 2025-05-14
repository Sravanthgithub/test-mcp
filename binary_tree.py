class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
