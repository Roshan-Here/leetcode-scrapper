import pytest
from q_1143_longestCommonSubsequence import Solution


@pytest.mark.parametrize(
    "text1, text2, output", [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0)]
)
class TestSolution:
    def test_longestCommonSubsequence(self, text1: str, text2: str, output: int):
        sc = Solution()
        assert (
            sc.longestCommonSubsequence(
                text1,
                text2,
            )
            == output
        )
