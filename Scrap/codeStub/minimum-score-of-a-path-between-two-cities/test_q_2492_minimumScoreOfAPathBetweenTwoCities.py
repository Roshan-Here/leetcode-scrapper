import pytest
from q_2492_minimumScoreOfAPathBetweenTwoCities import Solution


@pytest.mark.parametrize(
    "n, roads, output",
    [
        (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
    ],
)
class TestSolution:
    def test_minScore(self, n: int, roads: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minScore(
                n,
                roads,
            )
            == output
        )
