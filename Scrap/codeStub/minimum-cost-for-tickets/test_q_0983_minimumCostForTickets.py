import pytest
from q_0983_minimumCostForTickets import Solution


@pytest.mark.parametrize(
    "days, costs, output",
    [
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ],
)
class TestSolution:
    def test_mincostTickets(self, days: List[int], costs: List[int], output: int):
        sc = Solution()
        assert (
            sc.mincostTickets(
                days,
                costs,
            )
            == output
        )
