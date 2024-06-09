import pytest
from q_3153_sumOfDigitDifferencesOfAllPairs import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_sumDigitDifferences(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.sumDigitDifferences() == output
