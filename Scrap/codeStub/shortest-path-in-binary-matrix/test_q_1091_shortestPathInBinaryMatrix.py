import pytest
from q_1091_shortestPathInBinaryMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ],
)
class TestSolution:
    def test_shortestPathBinaryMatrix(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.shortestPathBinaryMatrix(
                grid,
            )
            == output
        )
