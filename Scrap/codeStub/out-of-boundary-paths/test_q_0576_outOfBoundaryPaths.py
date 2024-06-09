import pytest
from q_0576_outOfBoundaryPaths import Solution


@pytest.mark.parametrize(
    "m, n, maxMove, startRow, startColumn, output",
    [(2, 2, 2, 0, 0, 6), (1, 3, 3, 0, 1, 12)],
)
class TestSolution:
    def test_findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int, output: int
    ):
        sc = Solution()
        assert (
            sc.findPaths(
                m,
                n,
                maxMove,
                startRow,
                startColumn,
            )
            == output
        )
