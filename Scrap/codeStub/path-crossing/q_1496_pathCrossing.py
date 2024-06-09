front_matter = {
    "qid": 1496,
    "title": "Path Crossing",
    "titleSlug": "path-crossing",
    "difficulty": "Easy",
    "tags": ["Hash Table", "String"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

    Return `true` *if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited*. Return `false` otherwise.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png)
    ```
    Input: path = "NES"
    Output: false
    Explanation: Notice that the path doesn't cross any point more than once.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png)
    ```
    Input: path = "NESWW"
    Output: true
    Explanation: Notice that the path visits the origin twice.
    ```


    **Constraints:**

    * `1 <= path.length <= 10^{4}`
    * `path[i]` is either `'N'`, `'S'`, `'E'`, or `'W'`.
    """

    def isPathCrossing(self, path: str) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
