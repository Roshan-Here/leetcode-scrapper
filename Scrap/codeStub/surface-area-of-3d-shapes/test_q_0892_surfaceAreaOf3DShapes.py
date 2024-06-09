import pytest
from q_0892_surfaceAreaOf3DShapes import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 2], [3, 4]], 34),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
        ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46),
    ],
)
class TestSolution:
    def test_surfaceArea(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.surfaceArea(
                grid,
            )
            == output
        )
