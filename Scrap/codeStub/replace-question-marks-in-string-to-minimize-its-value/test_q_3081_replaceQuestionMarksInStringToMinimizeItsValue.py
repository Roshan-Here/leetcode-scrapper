import pytest
from q_3081_replaceQuestionMarksInStringToMinimizeItsValue import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimizeStringValue(self, s: str, output: str):
        sc = Solution()
        assert sc.minimizeStringValue() == output
