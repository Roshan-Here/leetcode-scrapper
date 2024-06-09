import pytest
from q_0010_regularExpressionMatching import Solution


@pytest.mark.parametrize(
    "s, p, output", [("aa", "a", False), ("aa", "a*", True), ("ab", ".*", True)]
)
class TestSolution:
    def test_isMatch(self, s: str, p: str, output: bool):
        sc = Solution()
        assert (
            sc.isMatch(
                s,
                p,
            )
            == output
        )
