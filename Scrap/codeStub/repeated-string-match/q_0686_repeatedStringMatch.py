front_matter = {
    "qid": 686,
    "title": "Repeated String Match",
    "titleSlug": "repeated-string-match",
    "difficulty": "Medium",
    "tags": ["String", "String Matching"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given two strings `a` and `b`, return *the minimum number of times you should repeat string* `a` *so that string* `b` *is a substring of it*. If it is impossible for `b`​​​​​​ to be a substring of `a` after repeating it, return `-1`.

    **Notice:** string `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"` and repeated 2 times is `"abcabc"`.



    **Example 1:**

    ```
    Input: a = "abcd", b = "cdabcdab"
    Output: 3
    Explanation: We return 3 because by repeating a three times "ab**cdabcdab**cd", b is a substring of it.
    ```
    **Example 2:**

    ```
    Input: a = "a", b = "aa"
    Output: 2
    ```


    **Constraints:**

    * `1 <= a.length, b.length <= 10^{4}`
    * `a` and `b` consist of lowercase English letters.
    """

    def repeatedStringMatch(self, a: str, b: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
