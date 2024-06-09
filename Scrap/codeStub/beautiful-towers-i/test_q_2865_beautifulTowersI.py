import pytest
from q_2865_beautifulTowersI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximumSumOfHeights(self, heights: List[int], output: int):
        sc = Solution()
        assert sc.maximumSumOfHeights() == output
