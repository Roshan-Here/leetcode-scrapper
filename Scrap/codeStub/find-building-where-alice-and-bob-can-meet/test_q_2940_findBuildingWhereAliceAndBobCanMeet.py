import pytest
from q_2940_findBuildingWhereAliceAndBobCanMeet import Solution


@pytest.mark.parametrize(
    "heights, queries, output",
    [
        (
            [6, 4, 8, 5, 2, 7],
            [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]],
            [2, 5, -1, 5, 2],
        ),
        (
            [5, 3, 8, 2, 6, 1, 4, 6],
            [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
            [7, 6, -1, 4, 6],
        ),
    ],
)
class TestSolution:
    def test_leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.leftmostBuildingQueries(
                heights,
                queries,
            )
            == output
        )
