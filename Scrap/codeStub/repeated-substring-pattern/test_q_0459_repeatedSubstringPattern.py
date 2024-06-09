import pytest
from q_0459_repeatedSubstringPattern import Solution


@pytest.mark.parametrize(
    "s, output", [("abab", True), ("aba", False), ("abcabcabcabc", True)]
)
class TestSolution:
    def test_repeatedSubstringPattern(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.repeatedSubstringPattern(
                s,
            )
            == output
        )
