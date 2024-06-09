import pytest
from q_0436_findRightInterval import Solution


@pytest.mark.parametrize(
    "intervals, output",
    [
        ([[1, 2]], [-1]),
        ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
        ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
    ],
)
class TestSolution:
    def test_findRightInterval(self, intervals: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findRightInterval(
                intervals,
            )
            == output
        )
