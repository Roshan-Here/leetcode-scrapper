import pytest
from q_1930_uniqueLength3PalindromicSubsequences import Solution


@pytest.mark.parametrize("s, output", [("aabca", 3), ("adc", 0), ("bbcbaba", 4)])
class TestSolution:
    def test_countPalindromicSubsequence(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countPalindromicSubsequence(
                s,
            )
            == output
        )
