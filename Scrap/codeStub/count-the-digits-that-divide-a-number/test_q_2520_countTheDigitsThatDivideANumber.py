import pytest
from q_2520_countTheDigitsThatDivideANumber import Solution


@pytest.mark.parametrize("num, output", [(7, 1), (121, 2), (1248, 4)])
class TestSolution:
    def test_countDigits(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.countDigits(
                num,
            )
            == output
        )
