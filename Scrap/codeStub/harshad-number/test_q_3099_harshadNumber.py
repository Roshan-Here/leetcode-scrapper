import pytest
from q_3099_harshadNumber import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_sumOfTheDigitsOfHarshadNumber(self, x: int, output: int):
        sc = Solution()
        assert sc.sumOfTheDigitsOfHarshadNumber() == output
