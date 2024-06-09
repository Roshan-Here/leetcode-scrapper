import pytest
from q_2862_maximumElementSumOfACompleteSubsetOfIndices import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximumSum(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.maximumSum() == output
