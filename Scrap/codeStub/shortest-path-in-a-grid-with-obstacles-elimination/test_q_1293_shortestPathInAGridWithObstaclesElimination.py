import pytest
from q_1293_shortestPathInAGridWithObstaclesElimination import Solution


@pytest.mark.parametrize(
    "grid, k, output",
    [
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6),
        ([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1),
    ],
)
class TestSolution:
    def test_shortestPath(self, grid: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.shortestPath(
                grid,
                k,
            )
            == output
        )
