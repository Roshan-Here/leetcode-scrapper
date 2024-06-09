front_matter = {
    "qid": 632,
    "title": "Smallest Range Covering Elements from K Lists",
    "titleSlug": "smallest-range-covering-elements-from-k-lists",
    "difficulty": "Hard",
    "tags": [
        "Array",
        "Hash Table",
        "Greedy",
        "Sliding Window",
        "Sorting",
        "Heap (Priority Queue)",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You have `k` lists of sorted integers in **non-decreasing order**. Find the **smallest** range that includes at least one number from each of the `k` lists.

    We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c` **or** `a < c` if `b - a == d - c`.



    **Example 1:**

    ```
    Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    Output: [20,24]
    Explanation:
    List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
    List 2: [0, 9, 12, 20], 20 is in range [20,24].
    List 3: [5, 18, 22, 30], 22 is in range [20,24].
    ```
    **Example 2:**

    ```
    Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
    Output: [1,1]
    ```


    **Constraints:**

    * `nums.length == k`
    * `1 <= k <= 3500`
    * `1 <= nums[i].length <= 50`
    * `-10^{5} <= nums[i][j] <= 10^{5}`
    * `nums[i]` is sorted in **non-decreasing** order.
    """

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
