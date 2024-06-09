import pytest
from q_0030_substringWithConcatenationOfAllWords import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findSubstring(self, s: str, words: List[str], output: List[int]):
        sc = Solution()
        assert sc.findSubstring() == output
