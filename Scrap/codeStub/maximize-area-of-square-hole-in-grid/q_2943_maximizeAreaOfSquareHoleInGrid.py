front_matter = {
    "qid": 2943,
    "title": "Maximize Area of Square Hole in Grid",
    "titleSlug": "maximize-area-of-square-hole-in-grid",
    "difficulty": "Medium",
    "tags": ["Array", "Sorting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given the two integers, `n` and `m` and two integer arrays, `hBars` and `vBars`. The grid has `n + 2` horizontal and `m + 2` vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from `1`.

    You can **remove** some of the bars in `hBars` from horizontal bars and some of the bars in `vBars` from vertical bars. Note that other bars are fixed and cannot be removed.

    Return an integer denoting the **maximum area** of a *square-shaped* hole in the grid, after removing some bars (possibly none).



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png)

    Input: n = 2, m = 1, hBars = [2,3], vBars = [2]

    Output: 4

    Explanation:

    The left image shows the initial grid formed by the bars. The horizontal bars are `[1,2,3,4]`, and the vertical bars are `[1,2,3]`.

    One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2023/11/04/screenshot-from-2023-11-04-17-01-02.png)

    Input: n = 1, m = 1, hBars = [2], vBars = [2]

    Output: 4

    Explanation:

    To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

    **Example 3:**

    ![](https://assets.leetcode.com/uploads/2024/03/12/unsaved-image-2.png)

    Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4]

    Output: 4

    Explanation:

    One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.



    **Constraints:**

    * `1 <= n <= 10^{9}`
    * `1 <= m <= 10^{9}`
    * `1 <= hBars.length <= 100`
    * `2 <= hBars[i] <= n + 1`
    * `1 <= vBars.length <= 100`
    * `2 <= vBars[i] <= m + 1`
    * All values in `hBars` are distinct.
    * All values in `vBars` are distinct.
    """

    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
