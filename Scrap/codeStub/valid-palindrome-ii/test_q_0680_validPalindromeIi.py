import pytest
from q_0680_validPalindromeIi import Solution


@pytest.mark.parametrize("s, output", [("aba", True), ("abca", True), ("abc", False)])
class TestSolution:
    def test_validPalindrome(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.validPalindrome(
                s,
            )
            == output
        )
