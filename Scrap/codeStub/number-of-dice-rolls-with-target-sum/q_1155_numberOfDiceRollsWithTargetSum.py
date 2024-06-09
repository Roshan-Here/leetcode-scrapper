front_matter = {
    "qid": 1155,
    "title": "Number of Dice Rolls With Target Sum",
    "titleSlug": "number-of-dice-rolls-with-target-sum",
    "difficulty": "Medium",
    "tags": ["Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You have `n` dice, and each dice has `k` faces numbered from `1` to `k`.

    Given three integers `n`, `k`, and `target`, return *the number of possible ways (out of the* `k^{n}` *total ways)* *to roll the dice, so the sum of the face-up numbers equals* `target`. Since the answer may be too large, return it **modulo** `10^{9} + 7`.



    **Example 1:**

    ```
    Input: n = 1, k = 6, target = 3
    Output: 1
    Explanation: You throw one die with 6 faces.
    There is only one way to get a sum of 3.
    ```
    **Example 2:**

    ```
    Input: n = 2, k = 6, target = 7
    Output: 6
    Explanation: You throw two dice, each with 6 faces.
    There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
    ```
    **Example 3:**

    ```
    Input: n = 30, k = 30, target = 500
    Output: 222616187
    Explanation: The answer must be returned modulo 10^{9} + 7.
    ```


    **Constraints:**

    * `1 <= n, k <= 30`
    * `1 <= target <= 1000`
    """

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.