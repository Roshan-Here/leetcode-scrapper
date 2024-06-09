front_matter = {
    "qid": 1631,
    "title": "Path With Minimum Effort",
    "titleSlug": "path-with-minimum-effort",
    "difficulty": "Medium",
    "tags": [
        "Array",
        "Binary Search",
        "Depth-First Search",
        "Breadth-First Search",
        "Union Find",
        "Heap (Priority Queue)",
        "Matrix",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**, **down**, **left**, or **right**, and you wish to find a route that requires the minimum **effort**.

    A route's **effort** is the **maximum absolute difference**in heights between two consecutive cells of the route.

    Return *the minimum **effort** required to travel from the top-left cell to the bottom-right cell.*



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/10/04/ex1.png)

    ```
    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
    This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2020/10/04/ex2.png)

    ```
    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
    ```
    **Example 3:**

    ![](https://assets.leetcode.com/uploads/2020/10/04/ex3.png)
    ```
    Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    Explanation: This route does not require any effort.
    ```


    **Constraints:**

    * `rows == heights.length`
    * `columns == heights[i].length`
    * `1 <= rows, columns <= 100`
    * `1 <= heights[i][j] <= 10^{6}`
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
