# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees
            
            for i in range(start, end + 1):
                # Buat semua kombinasi left tree dari [start, i-1]
                left_trees = build(start, i - 1)
                # Buat semua kombinasi right tree dari [i+1, end]
                right_trees = build(i + 1, end)

                # Gabungkan semua kemungkinan kombinasi left dan right dengan root i
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees
        
        return build(1, n)
