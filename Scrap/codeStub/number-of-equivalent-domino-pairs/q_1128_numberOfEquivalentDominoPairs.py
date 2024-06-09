front_matter = {
    "qid": 1128,
    "title": "Number of Equivalent Domino Pairs",
    "titleSlug": "number-of-equivalent-domino-pairs",
    "difficulty": "Easy",
    "tags": ["Array", "Hash Table", "Counting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`) - that is, one domino can be rotated to be equal to another domino.

    Return *the number of pairs* `(i, j)` *for which* `0 <= i < j < dominoes.length`*, and* `dominoes[i]` *is **equivalent to*** `dominoes[j]`.



    **Example 1:**

    ```
    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1
    ```
    **Example 2:**

    ```
    Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    Output: 3
    ```


    **Constraints:**

    * `1 <= dominoes.length <= 4 * 10^{4}`
    * `dominoes[i].length == 2`
    * `1 <= dominoes[i][j] <= 9`
    """

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
