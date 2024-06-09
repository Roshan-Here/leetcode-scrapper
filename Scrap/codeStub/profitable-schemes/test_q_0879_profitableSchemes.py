import pytest
from q_0879_profitableSchemes import Solution


@pytest.mark.parametrize(
    "n, minProfit, group, profit, output",
    [(5, 3, [2, 2], [2, 3], 2), (10, 5, [2, 3, 5], [6, 7, 8], 7)],
)
class TestSolution:
    def test_profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.profitableSchemes(
                n,
                minProfit,
                group,
                profit,
            )
            == output
        )
