import pytest
from q_0224_basicCalculator import Solution


@pytest.mark.parametrize(
    "s, output", [("1 + 1", 2), (" 2-1 + 2 ", 3), ("(1+(4+5+2)-3)+(6+8)", 23)]
)
class TestSolution:
    def test_calculate(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.calculate(
                s,
            )
            == output
        )
