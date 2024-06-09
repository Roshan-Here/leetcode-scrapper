import pytest
from q_0357_countNumbersWithUniqueDigits import Solution


@pytest.mark.parametrize("n, output", [(2, 91), (0, 1)])
class TestSolution:
    def test_countNumbersWithUniqueDigits(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countNumbersWithUniqueDigits(
                n,
            )
            == output
        )
