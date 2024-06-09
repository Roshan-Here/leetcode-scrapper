import pytest
from q_3142_checkIfGridSatisfiesConditions import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_satisfiesConditions(self, grid: List[List[int]], output: bool):
        sc = Solution()
        assert sc.satisfiesConditions() == output
