import pytest
from q_0847_shortestPathVisitingAllNodes import Solution


@pytest.mark.parametrize(
    "graph, output",
    [([[1, 2, 3], [0], [0], [0]], 4), ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4)],
)
class TestSolution:
    def test_shortestPathLength(self, graph: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.shortestPathLength(
                graph,
            )
            == output
        )
