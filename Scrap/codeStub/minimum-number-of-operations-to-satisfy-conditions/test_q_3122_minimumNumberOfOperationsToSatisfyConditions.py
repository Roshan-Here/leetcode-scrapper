import pytest
from q_3122_minimumNumberOfOperationsToSatisfyConditions import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumOperations(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert sc.minimumOperations() == output
