front_matter = {
    "qid": 2644,
    "title": "Find the Maximum Divisibility Score",
    "titleSlug": "find-the-maximum-divisibility-score",
    "difficulty": "Easy",
    "tags": ["Array"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given two integer arrays `nums` and `divisors`.

    The **divisibility score** of `divisors[i]` is the number of indices `j` such that `nums[j]` is divisible by `divisors[i]`.

    Return the integer `divisors[i]` with the **maximum** divisibility score. If multiple integers have the maximum score, return the smallest one.



    **Example 1:**

    Input: nums = [2,9,15,50], divisors = [5,3,7,2]

    Output: 2

    Explanation:

    The divisibility score of `divisors[0]` is 2 since `nums[2]` and `nums[3]` are divisible by 5.

    The divisibility score of `divisors[1]` is 1 since only `nums[1]` is divisible by 3.

    The divisibility score of `divisors[2]` is 0 since none of the numbers in `nums` is divisible by 7.

    The divisibility score of `divisors[3]` is 2 since `nums[0]` and `nums[3]` are divisible by 2.

    As `divisors[0]` and `divisors[3]` have the same divisibility score, we return the smaller one which is `divisors[3]`.

    **Example 2:**

    Input: nums = [4,7,9,3,9], divisors = [5,2,3]

    Output: 3

    Explanation:

    The divisibility score of `divisors[0]` is 0 since none of numbers in `nums` is divisible by 5.

    The divisibility score of `divisors[1]` is 1 since only `nums[0]` is divisible by 2.

    The divisibility score of `divisors[2]` is 3 since `nums[2]`, `nums[3]` and `nums[4]` are divisible by 3.

    **Example 3:**

    Input: nums = [20,14,21,10], divisors = [10,16,20]

    Output: 10

    Explanation:

    The divisibility score of `divisors[0]` is 0 since none of the numbers in `nums` is divisible by 10.

    The divisibility score of `divisors[1]` is 0 since none of the numbers in `nums` is divisible by 16.

    The divisibility score of `divisors[2]` is 0 since none of the numbers in `nums` is divisible by 20.

    As `divisors[0]`, `divisors[1]` and `divisors[2]` all have the same divisibility score, we return the smallest one which is `divisors[0]`.



    **Constraints:**

    * `1 <= nums.length, divisors.length <= 1000`
    * `1 <= nums[i], divisors[i] <= 10^{9}`
    """

    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
