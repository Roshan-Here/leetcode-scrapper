import pytest
from q_2856_minimumArrayLengthAfterPairRemovals import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minLengthAfterRemovals(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.minLengthAfterRemovals() == output
