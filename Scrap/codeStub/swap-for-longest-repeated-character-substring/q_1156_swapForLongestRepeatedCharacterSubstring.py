front_matter = {
    "qid": 1156,
    "title": "Swap For Longest Repeated Character Substring",
    "titleSlug": "swap-for-longest-repeated-character-substring",
    "difficulty": "Medium",
    "tags": ["Hash Table", "String", "Sliding Window"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `text`. You can swap two of the characters in the `text`.

    Return *the length of the longest substring with repeated characters*.



    **Example 1:**

    ```
    Input: text = "ababa"
    Output: 3
    Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
    ```
    **Example 2:**

    ```
    Input: text = "aaabaaa"
    Output: 6
    Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
    ```
    **Example 3:**

    ```
    Input: text = "aaaaa"
    Output: 5
    Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.
    ```


    **Constraints:**

    * `1 <= text.length <= 2 * 10^{4}`
    * `text` consist of lowercase English characters only.
    """

    def maxRepOpt1(self, text: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
