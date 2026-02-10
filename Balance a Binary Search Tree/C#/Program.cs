/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode BalanceBST(TreeNode root) {
        var nums = TreeToList(new List<int>(), root);
        return BuildBalancedTree(nums, 0, nums.Count - 1);
    }

    private List<int> TreeToList(List<int> list, TreeNode node){
        if(node != null){
            TreeToList(list, node.left);
            list.Add(node.val);
            TreeToList(list, node.right); 
        }
        return list;
    }

    private TreeNode BuildBalancedTree(List<int> nums, int low, int high){
        if(low > high){
            return null;
        }
        var middle = (low + high) / 2;
        var root = new TreeNode(nums[middle]);
        root.left = BuildBalancedTree(nums, low, middle - 1);
        root.right = BuildBalancedTree(nums, middle + 1, high);
        return root;
    }
}