import pytest
from q_1631_pathWithMinimumEffort import Solution


@pytest.mark.parametrize(
    "heights, output",
    [
        ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
        ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
        (
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ],
            0,
        ),
    ],
)
class TestSolution:
    def test_minimumEffortPath(self, heights: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumEffortPath(
                heights,
            )
            == output
        )
