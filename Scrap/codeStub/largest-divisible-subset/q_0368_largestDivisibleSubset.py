front_matter = {
    "qid": 368,
    "title": "Largest Divisible Subset",
    "titleSlug": "largest-divisible-subset",
    "difficulty": "Medium",
    "tags": ["Array", "Math", "Dynamic Programming", "Sorting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a set of **distinct** positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

    * `answer[i] % answer[j] == 0`, or
    * `answer[j] % answer[i] == 0`

    If there are multiple solutions, return any of them.



    **Example 1:**

    ```
    Input: nums = [1,2,3]
    Output: [1,2]
    Explanation: [1,3] is also accepted.
    ```
    **Example 2:**

    ```
    Input: nums = [1,2,4,8]
    Output: [1,2,4,8]
    ```


    **Constraints:**

    * `1 <= nums.length <= 1000`
    * `1 <= nums[i] <= 2 * 10^{9}`
    * All the integers in `nums` are **unique**.
    """

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
