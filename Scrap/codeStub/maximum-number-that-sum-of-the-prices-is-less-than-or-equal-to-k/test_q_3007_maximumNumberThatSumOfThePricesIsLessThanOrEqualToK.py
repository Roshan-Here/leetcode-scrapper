import pytest
from q_3007_maximumNumberThatSumOfThePricesIsLessThanOrEqualToK import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findMaximumNumber(self, k: int, x: int, output: int):
        sc = Solution()
        assert sc.findMaximumNumber() == output
