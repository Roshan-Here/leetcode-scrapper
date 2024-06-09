import pytest
from q_3107_minimumOperationsToMakeMedianOfArrayEqualToK import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minOperationsToMakeMedianK(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert sc.minOperationsToMakeMedianK() == output
