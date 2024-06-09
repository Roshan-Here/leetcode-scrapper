front_matter = {
    "qid": 3091,
    "title": "Apply Operations to Make Sum of Array Greater Than or Equal to k",
    "titleSlug": "apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k",
    "difficulty": "Medium",
    "tags": ["Math", "Greedy", "Enumeration"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **positive** integer `k`. Initially, you have an array `nums = [1]`.

    You can perform **any** of the following operations on the array **any** number of times (**possibly zero**):

    * Choose any element in the array and **increase** its value by `1`.
    * Duplicate any element in the array and add it to the end of the array.

    Return *the **minimum** number of operations required to make the **sum** of elements of the final array greater than or equal to* `k`.



    **Example 1:**

    Input: k = 11

    Output: 5

    Explanation:

    We can do the following operations on the array `nums = [1]`:

    * Increase the element by `1` three times. The resulting array is `nums = [4]`.
    * Duplicate the element two times. The resulting array is `nums = [4,4,4]`.

    The sum of the final array is `4 + 4 + 4 = 12` which is greater than or equal to `k = 11`.
    The total number of operations performed is `3 + 2 = 5`.

    **Example 2:**

    Input: k = 1

    Output: 0

    Explanation:

    The sum of the original array is already greater than or equal to `1`, so no operations are needed.



    **Constraints:**

    * `1 <= k <= 10^{5}`
    """

    def minOperations(self, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
