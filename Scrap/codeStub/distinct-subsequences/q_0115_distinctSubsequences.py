front_matter = {
    "qid": 115,
    "title": "Distinct Subsequences",
    "titleSlug": "distinct-subsequences",
    "difficulty": "Hard",
    "tags": ["String", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given two strings s and t, return *the number of distinct* ***subsequences*** *of* s *which equals* t.

    The test cases are generated so that the answer fits on a 32-bit signed integer.



    **Example 1:**

    ```
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from s.
    **rabb**b**it**
    **ra**b**bbit**
    **rab**b**bit**
    ```
    **Example 2:**

    ```
    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation:
    As shown below, there are 5 ways you can generate "bag" from s.
    **ba**b**g**bag
    **ba**bgba**g**
    **b**abgb**ag**
    ba**b**gb**ag**
    babg**bag**
    ```


    **Constraints:**

    * `1 <= s.length, t.length <= 1000`
    * `s` and `t` consist of English letters.
    """

    def numDistinct(self, s: str, t: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
