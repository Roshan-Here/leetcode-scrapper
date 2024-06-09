front_matter = {
    "qid": 2532,
    "title": "Time to Cross a Bridge",
    "titleSlug": "time-to-cross-a-bridge",
    "difficulty": "Hard",
    "tags": ["Array", "Heap (Priority Queue)", "Simulation"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There are `k` workers who want to move `n` boxes from the right (old) warehouse to the left (new) warehouse. You are given the two integers `n` and `k`, and a 2D integer array `time` of size `k x 4` where `time[i] = [righti, picki, lefti, puti]`.

    The warehouses are separated by a river and connected by a bridge. Initially, all `k` workers are waiting on the left side of the bridge. To move the boxes, the `i^{th}` worker can do the following:

    * Cross the bridge to the right side in `righti` minutes.
    * Pick a box from the right warehouse in `picki` minutes.
    * Cross the bridge to the left side in `lefti` minutes.
    * Put the box into the left warehouse in `puti` minutes.

    The `i^{th}` worker is **less efficient** than the j`^{th}` worker if either condition is met:

    * `lefti + righti > leftj + rightj`
    * `lefti + righti == leftj + rightj` and `i > j`

    The following rules regulate the movement of the workers through the bridge:

    * Only one worker can use the bridge at a time.
    * When the bridge is unused prioritize the **least efficient** worker on the right side to cross. If there are no workers on the right side, prioritize the **least efficient** worker on the left side to cross.

    Return the **elapsed minutes** at which the last box reaches the **left side of the bridge**.



    **Example 1:**

    Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]

    Output: 6

    Explanation:

    ```
    From 0 to 1 minutes: worker 2 crosses the bridge to the right.
    From 1 to 2 minutes: worker 2 picks up a box from the right warehouse.
    From 2 to 6 minutes: worker 2 crosses the bridge to the left.
    From 6 to 7 minutes: worker 2 puts a box at the left warehouse.
    The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left side of the bridge.
    ```

    **Example 2:**

    Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]

    Output: 50

    Explanation:

    ```
    From 0  to 10: worker 1 crosses the bridge to the right.
    From 10 to 20: worker 1 picks up a box from the right warehouse.
    From 10 to 11: worker 0 crosses the bridge to the right.
    From 11 to 20: worker 0 picks up a box from the right warehouse.
    From 20 to 30: worker 1 crosses the bridge to the left.
    From 30 to 40: worker 1 puts a box at the left warehouse.
    From 30 to 31: worker 0 crosses the bridge to the left.
    From 31 to 39: worker 0 puts a box at the left warehouse.
    From 39 to 40: worker 0 crosses the bridge to the right.
    From 40 to 49: worker 0 picks up a box from the right warehouse.
    From 49 to 50: worker 0 crosses the bridge to the left.
    ```



    **Constraints:**

    * `1 <= n, k <= 10^{4}`
    * `time.length == k`
    * `time[i].length == 4`
    * `1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000`
    """

    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
