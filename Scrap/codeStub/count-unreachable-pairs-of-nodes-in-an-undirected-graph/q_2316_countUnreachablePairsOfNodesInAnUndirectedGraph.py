front_matter = {
    "qid": 2316,
    "title": "Count Unreachable Pairs of Nodes in an Undirected Graph",
    "titleSlug": "count-unreachable-pairs-of-nodes-in-an-undirected-graph",
    "difficulty": "Medium",
    "tags": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an integer `n`. There is an **undirected** graph with `n` nodes, numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [ai, bi]` denotes that there exists an **undirected** edge connecting nodes `ai` and `bi`.

    Return *the **number of pairs** of different nodes that are **unreachable** from each other*.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2022/05/05/tc-3.png)
    ```
    Input: n = 3, edges = [[0,1],[0,2],[1,2]]
    Output: 0
    Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2022/05/05/tc-2.png)
    ```
    Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    Output: 14
    Explanation: There are 14 pairs of nodes that are unreachable from each other:
    [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
    Therefore, we return 14.
    ```


    **Constraints:**

    * `1 <= n <= 10^{5}`
    * `0 <= edges.length <= 2 * 10^{5}`
    * `edges[i].length == 2`
    * `0 <= ai, bi < n`
    * `ai != bi`
    * There are no repeated edges.
    """

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
