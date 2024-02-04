class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def isBalanced(root: TreeNode):
    def dfs(root):
        if not root: return [True, 0]

        left, right = dfs(root.left), dfs(root.right) 
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(11)

print(isBalanced(root))
