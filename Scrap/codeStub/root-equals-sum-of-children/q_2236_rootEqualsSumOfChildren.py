front_matter = {
    "qid": 2236,
    "title": "Root Equals Sum of Children",
    "titleSlug": "root-equals-sum-of-children",
    "difficulty": "Easy",
    "tags": ["Tree", "Binary Tree"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """You are given the `root` of a **binary tree** that consists of exactly `3` nodes: the root, its left child, and its right child.

    Return `true` *if the value of the root is equal to the **sum** of the values of its two children, or* `false` *otherwise*.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2022/04/08/graph3drawio.png)
    ```
    Input: root = [10,4,6]
    Output: true
    Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
    10 is equal to 4 + 6, so we return true.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2022/04/08/graph3drawio-1.png)
    ```
    Input: root = [5,3,1]
    Output: false
    Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
    5 is not equal to 3 + 1, so we return false.
    ```


    **Constraints:**

    * The tree consists only of the root, its left child, and its right child.
    * `-100 <= Node.val <= 100`
    """

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
