import pytest
from q_3111_minimumRectanglesToCoverPoints import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minRectanglesToCoverPoints(
        self, points: List[List[int]], w: int, output: int
    ):
        sc = Solution()
        assert sc.minRectanglesToCoverPoints() == output
