front_matter = {
    "qid": 354,
    "title": "Russian Doll Envelopes",
    "titleSlug": "russian-doll-envelopes",
    "difficulty": "Hard",
    "tags": ["Array", "Binary Search", "Dynamic Programming", "Sorting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and the height of an envelope.

    One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

    Return *the maximum number of envelopes you can Russian doll (i.e., put one inside the other)*.

    **Note:** You cannot rotate an envelope.



    **Example 1:**

    ```
    Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    Output: 3
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
    ```
    **Example 2:**

    ```
    Input: envelopes = [[1,1],[1,1],[1,1]]
    Output: 1
    ```


    **Constraints:**

    * `1 <= envelopes.length <= 10^{5}`
    * `envelopes[i].length == 2`
    * `1 <= wi, hi <= 10^{5}`
    """

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
