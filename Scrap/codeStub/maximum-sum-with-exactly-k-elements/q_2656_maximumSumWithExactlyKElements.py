front_matter = {
    "qid": 2656,
    "title": "Maximum Sum With Exactly K Elements ",
    "titleSlug": "maximum-sum-with-exactly-k-elements",
    "difficulty": "Easy",
    "tags": ["Array", "Greedy"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **0-indexed** integer array `nums` and an integer `k`. Your task is to perform the following operation **exactly** `k` times in order to maximize your score:

    1. Select an element `m` from `nums`.
    2. Remove the selected element `m` from the array.
    3. Add a new element with a value of `m + 1` to the array.
    4. Increase your score by `m`.

    Return *the maximum score you can achieve after performing the operation exactly* `k` *times.*



    **Example 1:**

    ```
    Input: nums = [1,2,3,4,5], k = 3
    Output: 18
    Explanation: We need to choose exactly 3 elements from nums to maximize the sum.
    For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
    For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
    For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
    So, we will return 18.
    It can be proven, that 18 is the maximum answer that we can achieve.
    ```
    **Example 2:**

    ```
    Input: nums = [5,5,5], k = 2
    Output: 11
    Explanation: We need to choose exactly 2 elements from nums to maximize the sum.
    For the first iteration, we choose 5. Then sum is 5 and nums = [5,5,6]
    For the second iteration, we choose 6. Then sum is 5 + 6 = 11 and nums = [5,5,7]
    So, we will return 11.
    It can be proven, that 11 is the maximum answer that we can achieve.
    ```


    **Constraints:**

    * `1 <= nums.length <= 100`
    * `1 <= nums[i] <= 100`
    * `1 <= k <= 100`



    .spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0;
    }
    .spoiler {overflow:hidden;}
    .spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
    .spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
    .spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}"""

    def maximizeSum(self, nums: List[int], k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
