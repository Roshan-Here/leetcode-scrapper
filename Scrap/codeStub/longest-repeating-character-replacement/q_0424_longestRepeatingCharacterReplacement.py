front_matter = {
    "qid": 424,
    "title": "Longest Repeating Character Replacement",
    "titleSlug": "longest-repeating-character-replacement",
    "difficulty": "Medium",
    "tags": ["Hash Table", "String", "Sliding Window"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

    Return *the length of the longest substring containing the same letter you can get after performing the above operations*.



    **Example 1:**

    ```
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.
    ```
    **Example 2:**

    ```
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achieve this answer too.
    ```


    **Constraints:**

    * `1 <= s.length <= 10^{5}`
    * `s` consists of only uppercase English letters.
    * `0 <= k <= s.length`
    """

    def characterReplacement(self, s: str, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
