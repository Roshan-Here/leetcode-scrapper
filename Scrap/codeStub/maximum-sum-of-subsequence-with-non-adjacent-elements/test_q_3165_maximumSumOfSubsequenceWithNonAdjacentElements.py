import pytest
from q_3165_maximumSumOfSubsequenceWithNonAdjacentElements import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximumSumSubsequence(
        self, nums: List[int], queries: List[List[int]], output: int
    ):
        sc = Solution()
        assert sc.maximumSumSubsequence() == output
