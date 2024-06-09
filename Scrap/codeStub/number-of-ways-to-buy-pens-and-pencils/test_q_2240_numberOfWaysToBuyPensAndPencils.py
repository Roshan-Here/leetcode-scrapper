import pytest
from q_2240_numberOfWaysToBuyPensAndPencils import Solution


@pytest.mark.parametrize(
    "total, cost1, cost2, output", [(20, 10, 5, 9), (5, 10, 10, 1)]
)
class TestSolution:
    def test_waysToBuyPensPencils(
        self, total: int, cost1: int, cost2: int, output: int
    ):
        sc = Solution()
        assert (
            sc.waysToBuyPensPencils(
                total,
                cost1,
                cost2,
            )
            == output
        )
