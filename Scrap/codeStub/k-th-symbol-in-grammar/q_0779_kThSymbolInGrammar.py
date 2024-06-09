front_matter = {
    "qid": 779,
    "title": "K-th Symbol in Grammar",
    "titleSlug": "k-th-symbol-in-grammar",
    "difficulty": "Medium",
    "tags": ["Math", "Bit Manipulation", "Recursion"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """We build a table of `n` rows (**1-indexed**). We start by writing `0` in the `1^{st}` row. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

    * For example, for `n = 3`, the `1^{st}` row is `0`, the `2^{nd}` row is `01`, and the `3^{rd}` row is `0110`.

    Given two integer `n` and `k`, return the `k^{th}` (**1-indexed**) symbol in the `n^{th}` row of a table of `n` rows.



    **Example 1:**

    ```
    Input: n = 1, k = 1
    Output: 0
    Explanation: row 1: 0
    ```
    **Example 2:**

    ```
    Input: n = 2, k = 1
    Output: 0
    Explanation:
    row 1: 0
    row 2: 01
    ```
    **Example 3:**

    ```
    Input: n = 2, k = 2
    Output: 1
    Explanation:
    row 1: 0
    row 2: 01
    ```


    **Constraints:**

    * `1 <= n <= 30`
    * `1 <= k <= 2^{n - 1}`
    """

    def kthGrammar(self, n: int, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
