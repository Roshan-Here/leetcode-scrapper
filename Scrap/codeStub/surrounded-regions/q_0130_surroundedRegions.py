front_matter = {
    "qid": 130,
    "title": "Surrounded Regions",
    "titleSlug": "surrounded-regions",
    "difficulty": "Medium",
    "tags": [
        "Array",
        "Depth-First Search",
        "Breadth-First Search",
        "Union Find",
        "Matrix",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

    * **Connect**: A cell is connected to adjacent cells horizontally or vertically.
    * **Region**: To form a region **connect every** `'O'` cell.
    * **Surround**: The region is surrounded with `'X'` cells if you can **connect the region** with `'X'` cells and none of the region cells are on the edge of the `board`.

    A **surrounded region is captured** by replacing all `'O'`s with `'X'`s in the input matrix `board`.



    **Example 1:**

    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    Explanation:

    ![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
    In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

    **Example 2:**

    Input: board = [["X"]]

    Output: [["X"]]



    **Constraints:**

    * `m == board.length`
    * `n == board[i].length`
    * `1 <= m, n <= 200`
    * `board[i][j]` is `'X'` or `'O'`.
    """

    def solve(self, board: List[List[str]]) -> None:
        pass
        """
        Do not return anything, modify board in-place instead.
        """

    # If you have multiple solutions, add them all here as methods of the same class.
