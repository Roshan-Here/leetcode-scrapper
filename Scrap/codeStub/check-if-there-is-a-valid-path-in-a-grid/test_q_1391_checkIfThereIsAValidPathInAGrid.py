import pytest
from q_1391_checkIfThereIsAValidPathInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[2, 4, 3], [6, 5, 2]], True),
        ([[1, 2, 1], [1, 2, 1]], False),
        ([[1, 1, 2]], False),
    ],
)
class TestSolution:
    def test_hasValidPath(self, grid: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.hasValidPath(
                grid,
            )
            == output
        )
