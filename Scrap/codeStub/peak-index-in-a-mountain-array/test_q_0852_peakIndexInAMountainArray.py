import pytest
from q_0852_peakIndexInAMountainArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_peakIndexInMountainArray(self, arr: List[int], output: int):
        sc = Solution()
        assert sc.peakIndexInMountainArray() == output
