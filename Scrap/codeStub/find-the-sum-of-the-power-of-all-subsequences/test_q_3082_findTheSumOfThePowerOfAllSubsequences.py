import pytest
from q_3082_findTheSumOfThePowerOfAllSubsequences import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_sumOfPower(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert sc.sumOfPower() == output
