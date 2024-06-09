import pytest
from q_2644_findTheMaximumDivisibilityScore import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maxDivScore(self, nums: List[int], divisors: List[int], output: int):
        sc = Solution()
        assert sc.maxDivScore() == output
