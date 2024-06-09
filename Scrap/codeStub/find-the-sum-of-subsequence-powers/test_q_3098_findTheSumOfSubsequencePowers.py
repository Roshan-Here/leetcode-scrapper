import pytest
from q_3098_findTheSumOfSubsequencePowers import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_sumOfPowers(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert sc.sumOfPowers() == output
