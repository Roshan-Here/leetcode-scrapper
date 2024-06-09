import pytest
from q_1828_queriesOnNumberOfPointsInsideACircle import Solution


@pytest.mark.parametrize(
    "points, queries, output",
    [
        (
            [[1, 3], [3, 3], [5, 3], [2, 2]],
            [[2, 3, 1], [4, 3, 1], [1, 1, 2]],
            [3, 2, 2],
        ),
        (
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
            [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]],
            [2, 3, 2, 4],
        ),
    ],
)
class TestSolution:
    def test_countPoints(
        self, points: List[List[int]], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.countPoints(
                points,
                queries,
            )
            == output
        )
