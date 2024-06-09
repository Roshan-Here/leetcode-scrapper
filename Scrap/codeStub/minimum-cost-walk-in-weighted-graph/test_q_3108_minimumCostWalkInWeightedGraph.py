import pytest
from q_3108_minimumCostWalkInWeightedGraph import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert sc.minimumCost() == output
