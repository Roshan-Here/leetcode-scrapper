front_matter = {
    "qid": 2645,
    "title": "Minimum Additions to Make Valid String",
    "titleSlug": "minimum-additions-to-make-valid-string",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming", "Stack", "Greedy"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `word` to which you can insert letters "a", "b" or "c" anywhere and any number of times, return *the minimum number of letters that must be inserted so that `word` becomes **valid**.*

    A string is called **valid** if it can be formed by concatenating the string "abc" several times.



    **Example 1:**

    ```
    Input: word = "b"
    Output: 2
    Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "b" to obtain the valid string "**a**b**c**".
    ```
    **Example 2:**

    ```
    Input: word = "aaa"
    Output: 6
    Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "a**bc**a**bc**a**bc**".
    ```
    **Example 3:**

    ```
    Input: word = "abc"
    Output: 0
    Explanation: word is already valid. No modifications are needed.
    ```


    **Constraints:**

    * `1 <= word.length <= 50`
    * `word` consists of letters "a", "b" and "c" only.
    """

    def addMinimum(self, word: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
