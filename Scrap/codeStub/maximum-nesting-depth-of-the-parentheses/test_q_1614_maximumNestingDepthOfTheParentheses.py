import pytest
from q_1614_maximumNestingDepthOfTheParentheses import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maxDepth(self, s: str, output: int):
        sc = Solution()
        assert sc.maxDepth() == output
