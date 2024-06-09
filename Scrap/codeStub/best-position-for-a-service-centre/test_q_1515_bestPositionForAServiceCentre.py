import pytest
from q_1515_bestPositionForAServiceCentre import Solution


@pytest.mark.parametrize(
    "positions, output",
    [([[0, 1], [1, 0], [1, 2], [2, 1]], 4.0), ([[1, 1], [3, 3]], 2.82843)],
)
class TestSolution:
    def test_getMinDistSum(self, positions: List[List[int]], output: float):
        sc = Solution()
        assert (
            sc.getMinDistSum(
                positions,
            )
            == output
        )
