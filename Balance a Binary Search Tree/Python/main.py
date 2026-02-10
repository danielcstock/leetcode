# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        nums = []
        self.inorder(root, nums)
        return self.buildBalancedTree(nums, 0, len(nums) - 1)
        
    def inorder(self, node, nums):
        """
        :type node: Optional[TreeNode]
        :rtype List[int]
        """
        if not node:
            return
        self.inorder(node.left, nums)
        nums.append(node.val)
        self.inorder(node.right, nums)

    def buildBalancedTree(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype Optional[TreeNode]
        """
        if low > high:
            return None
        middle = (low + high) // 2
        root = TreeNode(nums[middle])
        root.left = self.buildBalancedTree(nums, low, middle - 1)
        root.right = self.buildBalancedTree(nums, middle + 1, high)
        return root

root = TreeNode()
root.val = 1
root.right = TreeNode()
root.right.val = 2
root.right.right = TreeNode()
root.right.right.val = 3
root.right.right.right = TreeNode()
root.right.right.right.val = 4

balancer = Solution()
balancer.balanceBST(root)