import pytest
from q_0856_scoreOfParentheses import Solution


@pytest.mark.parametrize("s, output", [("()", 1), ("(())", 2), ("()()", 2)])
class TestSolution:
    def test_scoreOfParentheses(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.scoreOfParentheses(
                s,
            )
            == output
        )
