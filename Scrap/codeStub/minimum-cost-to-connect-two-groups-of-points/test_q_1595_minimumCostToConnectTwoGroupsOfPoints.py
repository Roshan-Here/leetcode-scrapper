import pytest
from q_1595_minimumCostToConnectTwoGroupsOfPoints import Solution


@pytest.mark.parametrize(
    "cost, output",
    [
        ([[15, 96], [36, 2]], 17),
        ([[1, 3, 5], [4, 1, 1], [1, 5, 3]], 4),
        ([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]], 10),
    ],
)
class TestSolution:
    def test_connectTwoGroups(self, cost: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.connectTwoGroups(
                cost,
            )
            == output
        )
