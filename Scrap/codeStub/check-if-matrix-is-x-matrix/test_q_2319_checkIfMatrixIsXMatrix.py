import pytest
from q_2319_checkIfMatrixIsXMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]], True),
        ([[5, 7, 0], [0, 3, 1], [0, 5, 0]], False),
    ],
)
class TestSolution:
    def test_checkXMatrix(self, grid: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.checkXMatrix(
                grid,
            )
            == output
        )
