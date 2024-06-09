front_matter = {
    "qid": 1400,
    "title": "Construct K Palindrome Strings",
    "titleSlug": "construct-k-palindrome-strings",
    "difficulty": "Medium",
    "tags": ["Hash Table", "String", "Greedy", "Counting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `s` and an integer `k`, return `true` *if you can use all the characters in* `s` *to construct* `k` *palindrome strings or* `false` *otherwise*.



    **Example 1:**

    ```
    Input: s = "annabelle", k = 2
    Output: true
    Explanation: You can construct two palindromes using all characters in s.
    Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
    ```
    **Example 2:**

    ```
    Input: s = "leetcode", k = 3
    Output: false
    Explanation: It is impossible to construct 3 palindromes using all the characters of s.
    ```
    **Example 3:**

    ```
    Input: s = "true", k = 4
    Output: true
    Explanation: The only possible solution is to put each character in a separate string.
    ```


    **Constraints:**

    * `1 <= s.length <= 10^{5}`
    * `s` consists of lowercase English letters.
    * `1 <= k <= 10^{5}`
    """

    def canConstruct(self, s: str, k: int) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
