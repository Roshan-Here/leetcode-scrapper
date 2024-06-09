import pytest
from q_0730_countDifferentPalindromicSubsequences import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("bccb", 6),
        ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba", 104860361),
    ],
)
class TestSolution:
    def test_countPalindromicSubsequences(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countPalindromicSubsequences(
                s,
            )
            == output
        )
