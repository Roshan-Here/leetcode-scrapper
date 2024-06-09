front_matter = {
    "qid": 1091,
    "title": "Shortest Path in Binary Matrix",
    "titleSlug": "shortest-path-in-binary-matrix",
    "difficulty": "Medium",
    "tags": ["Array", "Breadth-First Search", "Matrix"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path** in the matrix*. If there is no clear path, return `-1`.

    A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

    * All the visited cells of the path are `0`.
    * All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

    The **length of a clear path** is the number of visited cells of this path.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)
    ```
    Input: grid = [[0,1],[1,0]]
    Output: 2
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)
    ```
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4
    ```
    **Example 3:**

    ```
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1
    ```


    **Constraints:**

    * `n == grid.length`
    * `n == grid[i].length`
    * `1 <= n <= 100`
    * `grid[i][j] is 0 or 1`
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
