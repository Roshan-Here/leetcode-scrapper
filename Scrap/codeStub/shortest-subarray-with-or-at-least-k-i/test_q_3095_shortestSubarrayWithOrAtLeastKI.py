import pytest
from q_3095_shortestSubarrayWithOrAtLeastKI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumSubarrayLength(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert sc.minimumSubarrayLength() == output
