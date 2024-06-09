import pytest
from q_3102_minimizeManhattanDistances import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumDistance(self, points: List[List[int]], output: int):
        sc = Solution()
        assert sc.minimumDistance() == output
