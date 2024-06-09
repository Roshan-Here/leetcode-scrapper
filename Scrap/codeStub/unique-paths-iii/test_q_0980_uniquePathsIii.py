import pytest
from q_0980_uniquePathsIii import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
        ([[0, 1], [2, 0]], 0),
    ],
)
class TestSolution:
    def test_uniquePathsIII(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.uniquePathsIII(
                grid,
            )
            == output
        )
