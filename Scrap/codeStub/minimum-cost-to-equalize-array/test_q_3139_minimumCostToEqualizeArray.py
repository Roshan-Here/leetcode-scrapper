import pytest
from q_3139_minimumCostToEqualizeArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minCostToEqualizeArray(
        self, nums: List[int], cost1: int, cost2: int, output: int
    ):
        sc = Solution()
        assert sc.minCostToEqualizeArray() == output
