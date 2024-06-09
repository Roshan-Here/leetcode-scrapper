import pytest
from q_2812_findTheSafestPathInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
        ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
        ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
    ],
)
class TestSolution:
    def test_maximumSafenessFactor(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumSafenessFactor(
                grid,
            )
            == output
        )
