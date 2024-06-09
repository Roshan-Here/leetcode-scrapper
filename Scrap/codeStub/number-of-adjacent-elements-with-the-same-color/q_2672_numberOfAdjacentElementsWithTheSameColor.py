front_matter = {
    "qid": 2672,
    "title": "Number of Adjacent Elements With the Same Color",
    "titleSlug": "number-of-adjacent-elements-with-the-same-color",
    "difficulty": "Medium",
    "tags": ["Array"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an integer `n` representing an array `colors` of length `n` where all elements are set to 0's meaning **uncolored**. You are also given a 2D integer array `queries` where `queries[i] = [indexi, colori]`. For the `i^{th}` **query**:

    * Set `colors[indexi]` to `colori`.
    * Count adjacent pairs in `colors` set to the same color (regardless of `colori`).

    Return an array `answer` of the same length as `queries` where `answer[i]` is the answer to the `i^{th}` query.



    **Example 1:**

    Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

    Output: [0,1,1,0,2]

    Explanation:

    * Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.
    * After the 1^{st} query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.
    * After the 2^{nd} query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.
    * After the 3^{rd} query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.
    * After the 4^{th} query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.
    * After the 5^{th} query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.

    **Example 2:**

    Input: n = 1, queries = [[0,100000]]

    Output: [0]

    Explanation:

    After the 1^{st} query colors = [100000]. The count of adjacent pairs with the same color is 0.



    **Constraints:**

    * `1 <= n <= 10^{5}`
    * `1 <= queries.length <= 10^{5}`
    * `queries[i].length == 2`
    * `0 <= indexi <= n - 1`
    * `1 <=  colori <= 10^{5}`
    """

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
