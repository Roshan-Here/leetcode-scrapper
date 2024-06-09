import pytest
from q_1755_closestSubsequenceSum import Solution


@pytest.mark.parametrize(
    "nums, goal, output",
    [([5, -7, 3, 5], 6, 0), ([7, -9, 15, -2], -5, 1), ([1, 2, 3], -7, 7)],
)
class TestSolution:
    def test_minAbsDifference(self, nums: List[int], goal: int, output: int):
        sc = Solution()
        assert (
            sc.minAbsDifference(
                nums,
                goal,
            )
            == output
        )
