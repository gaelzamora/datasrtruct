class Node:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right= None
'''
    Input
        1
     2    3
   4  5     6  
 7   8

    Output
        1
     3    2
   6    5   4  
         8   7 
'''


def invertTree(root: Node):
    if not root: return None
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)

    return root