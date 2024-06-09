front_matter = {
    "qid": 3149,
    "title": "Find the Minimum Cost Array Permutation",
    "titleSlug": "find-the-minimum-cost-array-permutation",
    "difficulty": "Hard",
    "tags": ["Array", "Dynamic Programming", "Bit Manipulation", "Bitmask"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an array `nums` which is a permutation of `[0, 1, 2, ..., n - 1]`. The **score** of any permutation of `[0, 1, 2, ..., n - 1]` named `perm` is defined as:

    `score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|`

    Return the permutation `perm` which has the **minimum** possible score. If *multiple* permutations exist with this score, return the one that is lexicographically smallest among them.



    **Example 1:**

    Input: nums = [1,0,2]

    Output: [0,1,2]

    Explanation:

    **![](https://assets.leetcode.com/uploads/2024/04/04/example0gif.gif)**

    The lexicographically smallest permutation with minimum cost is `[0,1,2]`. The cost of this permutation is `|0 - 0| + |1 - 2| + |2 - 1| = 2`.

    **Example 2:**

    Input: nums = [0,2,1]

    Output: [0,2,1]

    Explanation:

    **![](https://assets.leetcode.com/uploads/2024/04/04/example1gif.gif)**

    The lexicographically smallest permutation with minimum cost is `[0,2,1]`. The cost of this permutation is `|0 - 1| + |2 - 2| + |1 - 0| = 2`.



    **Constraints:**

    * `2 <= n == nums.length <= 14`
    * `nums` is a permutation of `[0, 1, 2, ..., n - 1]`.
    """

    def findPermutation(self, nums: List[int]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.