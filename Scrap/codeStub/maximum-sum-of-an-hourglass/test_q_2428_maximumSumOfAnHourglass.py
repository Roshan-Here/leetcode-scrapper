import pytest
from q_2428_maximumSumOfAnHourglass import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]], 30),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 35),
    ],
)
class TestSolution:
    def test_maxSum(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxSum(
                grid,
            )
            == output
        )
