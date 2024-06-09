front_matter = {
    "qid": 1614,
    "title": "Maximum Nesting Depth of the Parentheses",
    "titleSlug": "maximum-nesting-depth-of-the-parentheses",
    "difficulty": "Easy",
    "tags": ["String", "Stack"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a **valid parentheses string** `s`, return the **nesting depth** of`s`. The nesting depth is the **maximum** number of nested parentheses.



    **Example 1:**

    Input: s = "(1+(2\*3)+((8)/4))+1"

    Output: 3

    Explanation:

    Digit 8 is inside of 3 nested parentheses in the string.

    **Example 2:**

    Input: s = "(1)+((2))+(((3)))"

    Output: 3

    Explanation:

    Digit 3 is inside of 3 nested parentheses in the string.

    **Example 3:**

    Input: s = "()(())((()()))"

    Output: 3



    **Constraints:**

    * `1 <= s.length <= 100`
    * `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
    * It is guaranteed that parentheses expression `s` is a VPS.
    """

    def maxDepth(self, s: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
