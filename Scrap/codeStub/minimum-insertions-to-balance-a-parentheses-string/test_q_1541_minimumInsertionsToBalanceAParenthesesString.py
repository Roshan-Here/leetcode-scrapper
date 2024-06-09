import pytest
from q_1541_minimumInsertionsToBalanceAParenthesesString import Solution


@pytest.mark.parametrize("s, output", [("(()))", 1), ("())", 0), ("))())(", 3)])
class TestSolution:
    def test_minInsertions(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minInsertions(
                s,
            )
            == output
        )
