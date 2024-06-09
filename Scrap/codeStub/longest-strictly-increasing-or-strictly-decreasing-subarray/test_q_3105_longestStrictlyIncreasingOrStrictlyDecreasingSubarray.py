import pytest
from q_3105_longestStrictlyIncreasingOrStrictlyDecreasingSubarray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_longestMonotonicSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.longestMonotonicSubarray() == output
