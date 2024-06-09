import pytest
from q_2249_countLatticePointsInsideACircle import Solution


@pytest.mark.parametrize(
    "circles, output", [([[2, 2, 1]], 5), ([[2, 2, 2], [3, 4, 1]], 16)]
)
class TestSolution:
    def test_countLatticePoints(self, circles: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countLatticePoints(
                circles,
            )
            == output
        )
