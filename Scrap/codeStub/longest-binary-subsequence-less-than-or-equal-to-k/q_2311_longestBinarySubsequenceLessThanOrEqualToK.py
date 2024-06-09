front_matter = {
    "qid": 2311,
    "title": "Longest Binary Subsequence Less Than or Equal to K",
    "titleSlug": "longest-binary-subsequence-less-than-or-equal-to-k",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming", "Greedy", "Memoization"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a binary string `s` and a positive integer `k`.

    Return *the length of the **longest** subsequence of* `s` *that makes up a **binary** number less than or equal to* `k`.

    Note:

    * The subsequence can contain **leading zeroes**.
    * The empty string is considered to be equal to `0`.
    * A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



    **Example 1:**

    ```
    Input: s = "1001010", k = 5
    Output: 5
    Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
    Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
    The length of this subsequence is 5, so 5 is returned.
    ```
    **Example 2:**

    ```
    Input: s = "00101001", k = 1
    Output: 6
    Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
    The length of this subsequence is 6, so 6 is returned.
    ```


    **Constraints:**

    * `1 <= s.length <= 1000`
    * `s[i]` is either `'0'` or `'1'`.
    * `1 <= k <= 10^{9}`
    """

    def longestSubsequence(self, s: str, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
