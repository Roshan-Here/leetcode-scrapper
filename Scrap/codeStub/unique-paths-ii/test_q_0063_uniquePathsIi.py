import pytest
from q_0063_uniquePathsIi import Solution


@pytest.mark.parametrize(
    "obstacleGrid, output",
    [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2), ([[0, 1], [0, 0]], 1)],
)
class TestSolution:
    def test_uniquePathsWithObstacles(self, obstacleGrid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.uniquePathsWithObstacles(
                obstacleGrid,
            )
            == output
        )
