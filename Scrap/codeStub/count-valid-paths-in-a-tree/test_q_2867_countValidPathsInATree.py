import pytest
from q_2867_countValidPathsInATree import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (5, [[1, 2], [1, 3], [2, 4], [2, 5]], 4),
        (6, [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]], 6),
    ],
)
class TestSolution:
    def test_countPaths(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countPaths(
                n,
                edges,
            )
            == output
        )
