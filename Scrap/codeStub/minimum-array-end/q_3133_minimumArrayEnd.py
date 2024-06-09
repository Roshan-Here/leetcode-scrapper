front_matter = {
    "qid": 3133,
    "title": "Minimum Array End",
    "titleSlug": "minimum-array-end",
    "difficulty": "Medium",
    "tags": ["Bit Manipulation"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given two integers `n` and `x`. You have to construct an array of **positive** integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1]` is **greater than** `nums[i]`, and the result of the bitwise `AND` operation between all elements of `nums` is `x`.

    Return the **minimum** possible value of `nums[n - 1]`.



    **Example 1:**

    Input: n = 3, x = 4

    Output: 6

    Explanation:

    `nums` can be `[4,5,6]` and its last element is 6.

    **Example 2:**

    Input: n = 2, x = 7

    Output: 15

    Explanation:

    `nums` can be `[7,15]` and its last element is 15.



    **Constraints:**

    * `1 <= n, x <= 10^{8}`
    """

    def minEnd(self, n: int, x: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
