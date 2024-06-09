import pytest
from q_2580_countWaysToGroupOverlappingRanges import Solution


@pytest.mark.parametrize(
    "ranges, output", [([[6, 10], [5, 15]], 2), ([[1, 3], [10, 20], [2, 5], [4, 8]], 4)]
)
class TestSolution:
    def test_countWays(self, ranges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countWays(
                ranges,
            )
            == output
        )
