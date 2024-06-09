import pytest
from q_2769_findTheMaximumAchievableNumber import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_theMaximumAchievableX(self, num: int, t: int, output: int):
        sc = Solution()
        assert sc.theMaximumAchievableX() == output
