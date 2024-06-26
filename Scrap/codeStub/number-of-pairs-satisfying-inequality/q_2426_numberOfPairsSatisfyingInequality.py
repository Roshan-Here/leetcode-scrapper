front_matter = {
    "qid": 2426,
    "title": "Number of Pairs Satisfying Inequality",
    "titleSlug": "number-of-pairs-satisfying-inequality",
    "difficulty": "Hard",
    "tags": [
        "Array",
        "Binary Search",
        "Divide and Conquer",
        "Binary Indexed Tree",
        "Segment Tree",
        "Merge Sort",
        "Ordered Set",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given two **0-indexed** integer arrays `nums1` and `nums2`, each of size `n`, and an integer `diff`. Find the number of **pairs** `(i, j)` such that:

    * `0 <= i < j <= n - 1` **and**
    * `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff`.

    Return *the **number of pairs** that satisfy the conditions.*



    **Example 1:**

    ```
    Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
    Output: 3
    Explanation:
    There are 3 pairs that satisfy the conditions:
    1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
    2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
    3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
    Therefore, we return 3.
    ```
    **Example 2:**

    ```
    Input: nums1 = [3,-1], nums2 = [-2,2], diff = -1
    Output: 0
    Explanation:
    Since there does not exist any pair that satisfies the conditions, we return 0.
    ```


    **Constraints:**

    * `n == nums1.length == nums2.length`
    * `2 <= n <= 10^{5}`
    * `-10^{4} <= nums1[i], nums2[i] <= 10^{4}`
    * `-10^{4} <= diff <= 10^{4}`
    """

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
