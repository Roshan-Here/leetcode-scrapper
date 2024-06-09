front_matter = {
    "qid": 2400,
    "title": "Number of Ways to Reach a Position After Exactly k Steps",
    "titleSlug": "number-of-ways-to-reach-a-position-after-exactly-k-steps",
    "difficulty": "Medium",
    "tags": ["Math", "Dynamic Programming", "Combinatorics"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given two **positive** integers `startPos` and `endPos`. Initially, you are standing at position `startPos` on an **infinite** number line. With one step, you can move either one position to the left, or one position to the right.

    Given a positive integer `k`, return *the number of **different** ways to reach the position* `endPos` *starting from* `startPos`*, such that you perform **exactly*** `k` *steps*. Since the answer may be very large, return it **modulo** `10^{9} + 7`.

    Two ways are considered different if the order of the steps made is not exactly the same.

    **Note** that the number line includes negative integers.



    **Example 1:**

    ```
    Input: startPos = 1, endPos = 2, k = 3
    Output: 3
    Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
    - 1 -> 2 -> 3 -> 2.
    - 1 -> 2 -> 1 -> 2.
    - 1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.
    ```
    **Example 2:**

    ```
    Input: startPos = 2, endPos = 5, k = 10
    Output: 0
    Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.
    ```


    **Constraints:**

    * `1 <= startPos, endPos, k <= 1000`
    """

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
