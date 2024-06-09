import pytest
from q_0032_longestValidParentheses import Solution


@pytest.mark.parametrize("s, output", [("(()", 2), (")()())", 4), ("", 0)])
class TestSolution:
    def test_longestValidParentheses(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.longestValidParentheses(
                s,
            )
            == output
        )
