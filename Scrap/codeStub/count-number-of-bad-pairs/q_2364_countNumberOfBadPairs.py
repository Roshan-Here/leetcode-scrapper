front_matter = {
    "qid": 2364,
    "title": "Count Number of Bad Pairs",
    "titleSlug": "count-number-of-bad-pairs",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

    Return *the total number of **bad pairs** in* `nums`.



    **Example 1:**

    ```
    Input: nums = [4,1,3,3]
    Output: 5
    Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
    The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
    The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
    The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
    The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
    There are a total of 5 bad pairs, so we return 5.
    ```
    **Example 2:**

    ```
    Input: nums = [1,2,3,4,5]
    Output: 0
    Explanation: There are no bad pairs.
    ```


    **Constraints:**

    * `1 <= nums.length <= 10^{5}`
    * `1 <= nums[i] <= 10^{9}`
    """

    def countBadPairs(self, nums: List[int]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
