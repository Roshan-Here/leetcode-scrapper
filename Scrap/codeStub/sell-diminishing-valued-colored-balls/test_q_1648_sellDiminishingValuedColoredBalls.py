import pytest
from q_1648_sellDiminishingValuedColoredBalls import Solution


@pytest.mark.parametrize(
    "inventory, orders, output", [([2, 5], 4, 14), ([3, 5], 6, 19)]
)
class TestSolution:
    def test_maxProfit(self, inventory: List[int], orders: int, output: int):
        sc = Solution()
        assert (
            sc.maxProfit(
                inventory,
                orders,
            )
            == output
        )
