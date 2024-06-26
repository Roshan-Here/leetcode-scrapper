front_matter = {
    "qid": 241,
    "title": "Different Ways to Add Parentheses",
    "titleSlug": "different-ways-to-add-parentheses",
    "difficulty": "Medium",
    "tags": ["Math", "String", "Dynamic Programming", "Recursion", "Memoization"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `expression` of numbers and operators, return *all possible results from computing all the different possible ways to group numbers and operators*. You may return the answer in **any order**.

    The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed `10^{4}`.



    **Example 1:**

    ```
    Input: expression = "2-1-1"
    Output: [0,2]
    Explanation:
    ((2-1)-1) = 0
    (2-(1-1)) = 2
    ```
    **Example 2:**

    ```
    Input: expression = "2*3-4*5"
    Output: [-34,-14,-10,-10,10]
    Explanation:
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    ```


    **Constraints:**

    * `1 <= expression.length <= 20`
    * `expression` consists of digits and the operator `'+'`, `'-'`, and `'*'`.
    * All the integer values in the input expression are in the range `[0, 99]`.
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
