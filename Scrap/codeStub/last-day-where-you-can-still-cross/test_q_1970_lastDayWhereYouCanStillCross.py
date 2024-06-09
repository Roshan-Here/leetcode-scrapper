import pytest
from q_1970_lastDayWhereYouCanStillCross import Solution


@pytest.mark.parametrize(
    "row, col, cells, output",
    [
        (2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]], 2),
        (2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]], 1),
        (
            3,
            3,
            [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]],
            3,
        ),
    ],
)
class TestSolution:
    def test_latestDayToCross(
        self, row: int, col: int, cells: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.latestDayToCross(
                row,
                col,
                cells,
            )
            == output
        )
