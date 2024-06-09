front_matter = {
    "qid": 282,
    "title": "Expression Add Operators",
    "titleSlug": "expression-add-operators",
    "difficulty": "Hard",
    "tags": ["Math", "String", "Backtracking"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `num` that contains only digits and an integer `target`, return ***all possibilities** to insert the binary operators* `'+'`*,* `'-'`*, and/or* `'*'` *between the digits of* `num` *so that the resultant expression evaluates to the* `target` *value*.

    Note that operands in the returned expressions **should not** contain leading zeros.



    **Example 1:**

    ```
    Input: num = "123", target = 6
    Output: ["1*2*3","1+2+3"]
    Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
    ```
    **Example 2:**

    ```
    Input: num = "232", target = 8
    Output: ["2*3+2","2+3*2"]
    Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
    ```
    **Example 3:**

    ```
    Input: num = "3456237490", target = 9191
    Output: []
    Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
    ```


    **Constraints:**

    * `1 <= num.length <= 10`
    * `num` consists of only digits.
    * `-2^{31} <= target <= 2^{31} - 1`
    """

    def addOperators(self, num: str, target: int) -> List[str]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
