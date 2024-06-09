import pytest
from q_2484_countPalindromicSubsequences import Solution


@pytest.mark.parametrize(
    "s, output", [("103301", 2), ("0000000", 21), ("9999900000", 2)]
)
class TestSolution:
    def test_countPalindromes(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countPalindromes(
                s,
            )
            == output
        )
