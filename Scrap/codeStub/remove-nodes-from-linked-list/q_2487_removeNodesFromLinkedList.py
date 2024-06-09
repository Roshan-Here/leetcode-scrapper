front_matter = {
    "qid": 2487,
    "title": "Remove Nodes From Linked List",
    "titleSlug": "remove-nodes-from-linked-list",
    "difficulty": "Medium",
    "tags": ["Linked List", "Stack", "Recursion", "Monotonic Stack"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """You are given the `head` of a linked list.

    Remove every node which has a node with a greater value anywhere to the right side of it.

    Return *the* `head` *of the modified linked list.*



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2022/10/02/drawio.png)
    ```
    Input: head = [5,2,13,3,8]
    Output: [13,8]
    Explanation: The nodes that should be removed are 5, 2 and 3.
    - Node 13 is to the right of node 5.
    - Node 13 is to the right of node 2.
    - Node 8 is to the right of node 3.
    ```
    **Example 2:**

    ```
    Input: head = [1,1,1,1]
    Output: [1,1,1,1]
    Explanation: Every node has value 1, so no nodes are removed.
    ```


    **Constraints:**

    * The number of the nodes in the given list is in the range `[1, 10^{5}]`.
    * `1 <= Node.val <= 10^{5}`
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
