import pytest
from q_3143_maximumPointsInsideTheSquare import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maxPointsInsideSquare(self, points: List[List[int]], s: str, output: int):
        sc = Solution()
        assert sc.maxPointsInsideSquare() == output
