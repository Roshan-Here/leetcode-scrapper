front_matter = {
    "qid": 1582,
    "title": "Special Positions in a Binary Matrix",
    "titleSlug": "special-positions-in-a-binary-matrix",
    "difficulty": "Easy",
    "tags": ["Array", "Matrix"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an `m x n` binary matrix `mat`, return *the number of special positions in* `mat`*.*

    A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/12/23/special1.jpg)
    ```
    Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
    Output: 1
    Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg)
    ```
    Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
    ```


    **Constraints:**

    * `m == mat.length`
    * `n == mat[i].length`
    * `1 <= m, n <= 100`
    * `mat[i][j]` is either `0` or `1`.
    """

    def numSpecial(self, mat: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
