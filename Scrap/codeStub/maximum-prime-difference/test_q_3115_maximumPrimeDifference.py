import pytest
from q_3115_maximumPrimeDifference import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximumPrimeDifference(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.maximumPrimeDifference() == output
