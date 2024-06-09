import pytest
from q_2876_countVisitedNodesInADirectedGraph import Solution


@pytest.mark.parametrize(
    "edges, output", [([1, 2, 0, 0], [3, 3, 3, 4]), ([1, 2, 3, 4, 0], [5, 5, 5, 5, 5])]
)
class TestSolution:
    def test_countVisitedNodes(self, edges: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.countVisitedNodes(
                edges,
            )
            == output
        )
