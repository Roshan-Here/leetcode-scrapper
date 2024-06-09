import pytest
from q_2532_timeToCrossABridge import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findCrossingTime(self, n: int, k: int, time: List[List[int]], output: int):
        sc = Solution()
        assert sc.findCrossingTime() == output
