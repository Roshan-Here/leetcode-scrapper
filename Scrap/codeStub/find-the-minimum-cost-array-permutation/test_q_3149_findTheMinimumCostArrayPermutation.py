import pytest
from q_3149_findTheMinimumCostArrayPermutation import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findPermutation(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert sc.findPermutation() == output
