import pytest
from q_3154_findNumberOfWaysToReachTheKThStair import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_waysToReachStair(self, k: int, output: int):
        sc = Solution()
        assert sc.waysToReachStair() == output
