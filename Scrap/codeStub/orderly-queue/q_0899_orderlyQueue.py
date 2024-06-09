front_matter = {
    "qid": 899,
    "title": "Orderly Queue",
    "titleSlug": "orderly-queue",
    "difficulty": "Hard",
    "tags": ["Math", "String", "Sorting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `s` and an integer `k`. You can choose one of the first `k` letters of `s` and append it at the end of the string.

    Return *the lexicographically smallest string you could have after applying the mentioned step any number of moves*.



    **Example 1:**

    ```
    Input: s = "cba", k = 1
    Output: "acb"
    Explanation:
    In the first move, we move the 1^{st} character 'c' to the end, obtaining the string "bac".
    In the second move, we move the 1^{st} character 'b' to the end, obtaining the final result "acb".
    ```
    **Example 2:**

    ```
    Input: s = "baaca", k = 3
    Output: "aaabc"
    Explanation:
    In the first move, we move the 1^{st} character 'b' to the end, obtaining the string "aacab".
    In the second move, we move the 3^{rd} character 'c' to the end, obtaining the final result "aaabc".
    ```


    **Constraints:**

    * `1 <= k <= s.length <= 1000`
    * `s` consist of lowercase English letters.
    """

    def orderlyQueue(self, s: str, k: int) -> str:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
