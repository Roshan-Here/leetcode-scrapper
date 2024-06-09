import pytest
from q_3110_scoreOfAString import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_scoreOfString(self, s: str, output: int):
        sc = Solution()
        assert sc.scoreOfString() == output
