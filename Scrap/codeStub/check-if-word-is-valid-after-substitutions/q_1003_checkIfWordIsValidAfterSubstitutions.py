front_matter = {
    "qid": 1003,
    "title": "Check If Word Is Valid After Substitutions",
    "titleSlug": "check-if-word-is-valid-after-substitutions",
    "difficulty": "Medium",
    "tags": ["String", "Stack"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `s`, determine if it is **valid**.

    A string `s` is **valid** if, starting with an empty string `t = ""`, you can **transform** `t` **into** `s` after performing the following operation **any number of times**:

    * Insert string `"abc"` into any position in `t`. More formally, `t` becomes `tleft + "abc" + tright`, where `t == tleft + tright`. Note that `tleft` and `tright` may be **empty**.

    Return `true` *if* `s` *is a **valid** string, otherwise, return* `false`.



    **Example 1:**

    ```
    Input: s = "aabcbc"
    Output: true
    Explanation:
    "" -> "abc" -> "aabcbc"
    Thus, "aabcbc" is valid.
    ```
    **Example 2:**

    ```
    Input: s = "abcabcababcc"
    Output: true
    Explanation:
    "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
    Thus, "abcabcababcc" is valid.
    ```
    **Example 3:**

    ```
    Input: s = "abccba"
    Output: false
    Explanation: It is impossible to get "abccba" using the operation.
    ```


    **Constraints:**

    * `1 <= s.length <= 2 * 10^{4}`
    * `s` consists of letters `'a'`, `'b'`, and `'c'`
    """

    def isValid(self, s: str) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
