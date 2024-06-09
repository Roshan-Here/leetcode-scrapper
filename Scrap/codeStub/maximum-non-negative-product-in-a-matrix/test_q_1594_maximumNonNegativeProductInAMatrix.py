import pytest
from q_1594_maximumNonNegativeProductInAMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]], -1),
        ([[1, -2, 1], [1, -2, 1], [3, -4, 1]], 8),
        ([[1, 3], [0, -4]], 0),
    ],
)
class TestSolution:
    def test_maxProductPath(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxProductPath(
                grid,
            )
            == output
        )
