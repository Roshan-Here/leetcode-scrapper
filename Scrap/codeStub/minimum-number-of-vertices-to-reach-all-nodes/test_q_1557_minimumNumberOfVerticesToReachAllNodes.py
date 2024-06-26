import pytest
from q_1557_minimumNumberOfVerticesToReachAllNodes import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]], [0, 3]),
        (5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]], [0, 2, 3]),
    ],
)
class TestSolution:
    def test_findSmallestSetOfVertices(
        self, n: int, edges: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findSmallestSetOfVertices(
                n,
                edges,
            )
            == output
        )
