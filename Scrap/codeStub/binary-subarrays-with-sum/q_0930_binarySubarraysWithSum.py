front_matter = {
    "qid": 930,
    "title": "Binary Subarrays With Sum",
    "titleSlug": "binary-subarrays-with-sum",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table", "Sliding Window", "Prefix Sum"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a binary array `nums` and an integer `goal`, return *the number of non-empty **subarrays** with a sum* `goal`.

    A **subarray** is a contiguous part of the array.



    **Example 1:**

    ```

    Input: nums = [1,0,1,0,1], goal = 2
    Output: 4
    Explanation: The 4 subarrays are bolded and underlined below:
    [**1,0,1**,0,1]
    [**1,0,1,0**,1]
    [1,**0,1,0,1**]
    [1,0,**1,0,1**]
    ```
    **Example 2:**

    ```

    Input: nums = [0,0,0,0,0], goal = 0
    Output: 15
    ```


    **Constraints:**

    * `1 <= nums.length <= 3 * 10^{4}`
    * `nums[i]` is either `0` or `1`.
    * `0 <= goal <= nums.length`"""

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
