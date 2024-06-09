front_matter = {
    "qid": 2956,
    "title": "Find Common Elements Between Two Arrays",
    "titleSlug": "find-common-elements-between-two-arrays",
    "difficulty": "Easy",
    "tags": ["Array", "Hash Table"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given two integer arrays `nums1` and `nums2` of sizes `n` and `m`, respectively. Calculate the following values:

    * `answer1` : the number of indices `i` such that `nums1[i]` exists in `nums2`.
    * `answer2` : the number of indices `i` such that `nums2[i]` exists in `nums1`.

    Return `[answer1,answer2]`.



    **Example 1:**

    Input: nums1 = [2,3,2], nums2 = [1,2]

    Output: [2,1]

    Explanation:

    ![](https://assets.leetcode.com/uploads/2024/05/26/3488_find_common_elements_between_two_arrays-t1.gif)

    **Example 2:**

    Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

    Output: [3,4]

    Explanation:

    The elements at indices 1, 2, and 3 in `nums1` exist in `nums2` as well. So `answer1` is 3.

    The elements at indices 0, 1, 3, and 4 in `nums2` exist in `nums1`. So `answer2` is 4.

    **Example 3:**

    Input: nums1 = [3,4,2,3], nums2 = [1,5]

    Output: [0,0]

    Explanation:

    No numbers are common between `nums1` and `nums2`, so answer is [0,0].



    **Constraints:**

    * `n == nums1.length`
    * `m == nums2.length`
    * `1 <= n, m <= 100`
    * `1 <= nums1[i], nums2[i] <= 100`
    """

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
