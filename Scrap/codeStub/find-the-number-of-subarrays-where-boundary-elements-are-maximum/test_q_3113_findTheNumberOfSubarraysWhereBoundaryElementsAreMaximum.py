import pytest
from q_3113_findTheNumberOfSubarraysWhereBoundaryElementsAreMaximum import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfSubarrays(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.numberOfSubarrays() == output
