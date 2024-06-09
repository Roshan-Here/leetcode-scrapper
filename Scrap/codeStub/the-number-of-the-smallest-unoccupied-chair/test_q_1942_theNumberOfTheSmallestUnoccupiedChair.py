import pytest
from q_1942_theNumberOfTheSmallestUnoccupiedChair import Solution


@pytest.mark.parametrize(
    "times, targetFriend, output",
    [([[1, 4], [2, 3], [4, 6]], 1, 1), ([[3, 10], [1, 5], [2, 6]], 0, 2)],
)
class TestSolution:
    def test_smallestChair(
        self, times: List[List[int]], targetFriend: int, output: int
    ):
        sc = Solution()
        assert (
            sc.smallestChair(
                times,
                targetFriend,
            )
            == output
        )
