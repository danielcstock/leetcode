# Balance a Binary Search Tree (BST)

Given the `root` of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than `1`.

## Example 1:
![alt text](image.png)

> **Input**: root = [1,null,2,null,3,null,4,null,null]
>
> **Output**: [2,1,3,null,null,null,4]
>
> **Explanation**: This is not the only correct answer, [3,1,4,null,2] is also correct.

## Example 2:
![alt text](image-1.png)

> **Input**: root = [2,1,3]
>
> **Output**: [2,1,3]
 
## Constraints:
- The number of nodes in the tree is in the range [1, 104].
- `1 <= Node.val <= 105`

## Solution
The first step is to transform the tree into a sorted list of integers.
We do this by calling a function that recursively traverses the tree and adds each node’s value to a list, visiting all nodes on the left side first and then the right side.

Once the sorted list is built, we call the function that creates the balanced tree, passing the `low` and `high` parameters, which represent the starting and ending indexes of the list.

This second function first checks whether `low` is greater than `high`. If it is, it returns `null`. Otherwise, it finds the middle element of the list and creates a node with that value. Then, it recursively calls itself for the left half of the list and again for the right half. This ensures that each subtree is balanced, with its root chosen from the middle of the corresponding sublist.