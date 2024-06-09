front_matter = {
    "qid": 2386,
    "title": "Find the K-Sum of an Array",
    "titleSlug": "find-the-k-sum-of-an-array",
    "difficulty": "Hard",
    "tags": ["Array", "Sorting", "Heap (Priority Queue)"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an integer array `nums` and a **positive** integer `k`. You can choose any **subsequence** of the array and sum all of its elements together.

    We define the **K-Sum** of the array as the `k^{th}` **largest** subsequence sum that can be obtained (**not** necessarily distinct).

    Return *the K-Sum of the array*.

    A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    **Note** that the empty subsequence is considered to have a sum of `0`.



    **Example 1:**

    ```
    Input: nums = [2,4,-2], k = 5
    Output: 2
    Explanation: All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
    - 6, 4, 4, 2, 2, 0, 0, -2.
    The 5-Sum of the array is 2.
    ```
    **Example 2:**

    ```
    Input: nums = [1,-2,3,4,-10,12], k = 16
    Output: 10
    Explanation: The 16-Sum of the array is 10.
    ```


    **Constraints:**

    * `n == nums.length`
    * `1 <= n <= 10^{5}`
    * `-10^{9} <= nums[i] <= 10^{9}`
    * `1 <= k <= min(2000, 2^{n})`
    """

    def kSum(self, nums: List[int], k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
