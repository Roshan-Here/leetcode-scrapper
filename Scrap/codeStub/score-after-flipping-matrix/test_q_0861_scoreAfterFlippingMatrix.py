import pytest
from q_0861_scoreAfterFlippingMatrix import Solution


@pytest.mark.parametrize(
    "grid, output", [([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]], 39), ([[0]], 1)]
)
class TestSolution:
    def test_matrixScore(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.matrixScore(
                grid,
            )
            == output
        )
