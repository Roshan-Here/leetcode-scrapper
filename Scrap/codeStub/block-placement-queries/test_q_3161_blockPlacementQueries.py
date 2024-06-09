import pytest
from q_3161_blockPlacementQueries import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_getResults(self, queries: List[List[int]], output: List[bool]):
        sc = Solution()
        assert sc.getResults() == output
