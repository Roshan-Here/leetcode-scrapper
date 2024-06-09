import pytest
from q_2567_minimumScoreByChangingTwoElements import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimizeSum(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.minimizeSum() == output
