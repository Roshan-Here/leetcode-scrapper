front_matter = {
    "qid": 542,
    "title": "01 Matrix",
    "titleSlug": "01-matrix",
    "difficulty": "Medium",
    "tags": ["Array", "Dynamic Programming", "Breadth-First Search", "Matrix"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an `m x n` binary matrix `mat`, return *the distance of the nearest* `0` *for each cell*.

    The distance between two adjacent cells is `1`.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)
    ```
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)
    ```
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
    ```


    **Constraints:**

    * `m == mat.length`
    * `n == mat[i].length`
    * `1 <= m, n <= 10^{4}`
    * `1 <= m * n <= 10^{4}`
    * `mat[i][j]` is either `0` or `1`.
    * There is at least one `0` in `mat`.
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
