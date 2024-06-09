import pytest
from q_3097_shortestSubarrayWithOrAtLeastKIi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumSubarrayLength(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert sc.minimumSubarrayLength() == output
