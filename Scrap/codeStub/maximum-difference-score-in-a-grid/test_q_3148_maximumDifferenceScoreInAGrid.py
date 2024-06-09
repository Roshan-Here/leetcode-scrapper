import pytest
from q_3148_maximumDifferenceScoreInAGrid import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maxScore(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert sc.maxScore() == output
