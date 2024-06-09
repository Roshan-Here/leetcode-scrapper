import pytest
from q_2815_maxPairSumInAnArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maxSum(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.maxSum() == output
