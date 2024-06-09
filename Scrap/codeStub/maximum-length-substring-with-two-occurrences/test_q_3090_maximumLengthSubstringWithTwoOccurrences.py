import pytest
from q_3090_maximumLengthSubstringWithTwoOccurrences import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximumLengthSubstring(self, s: str, output: int):
        sc = Solution()
        assert sc.maximumLengthSubstring() == output
