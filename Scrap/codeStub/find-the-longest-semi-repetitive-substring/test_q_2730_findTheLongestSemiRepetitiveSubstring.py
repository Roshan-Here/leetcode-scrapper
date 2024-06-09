import pytest
from q_2730_findTheLongestSemiRepetitiveSubstring import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_longestSemiRepetitiveSubstring(self, s: str, output: int):
        sc = Solution()
        assert sc.longestSemiRepetitiveSubstring() == output
