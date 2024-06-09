front_matter = {
    "qid": 3159,
    "title": "Find Occurrences of an Element in an Array",
    "titleSlug": "find-occurrences-of-an-element-in-an-array",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an integer array `nums`, an integer array `queries`, and an integer `x`.

    For each `queries[i]`, you need to find the index of the `queries[i]^{th}` occurrence of `x` in the `nums` array. If there are fewer than `queries[i]` occurrences of `x`, the answer should be -1 for that query.

    Return an integer array `answer` containing the answers to all queries.



    **Example 1:**

    Input: nums = [1,3,1,7], queries = [1,3,2,4], x = 1

    Output: [0,-1,2,-1]

    Explanation:

    * For the 1^{st} query, the first occurrence of 1 is at index 0.
    * For the 2^{nd} query, there are only two occurrences of 1 in `nums`, so the answer is -1.
    * For the 3^{rd} query, the second occurrence of 1 is at index 2.
    * For the 4^{th} query, there are only two occurrences of 1 in `nums`, so the answer is -1.

    **Example 2:**

    Input: nums = [1,2,3], queries = [10], x = 5

    Output: [-1]

    Explanation:

    * For the 1^{st} query, 5 doesn't exist in `nums`, so the answer is -1.



    **Constraints:**

    * `1 <= nums.length, queries.length <= 10^{5}`
    * `1 <= queries[i] <= 10^{5}`
    * `1 <= nums[i], x <= 10^{4}`
    """

    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
