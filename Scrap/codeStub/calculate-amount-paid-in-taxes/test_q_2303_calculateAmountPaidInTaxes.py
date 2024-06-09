import pytest
from q_2303_calculateAmountPaidInTaxes import Solution


@pytest.mark.parametrize(
    "brackets, income, output",
    [
        ([[3, 50], [7, 10], [12, 25]], 10, 2.65),
        ([[1, 0], [4, 25], [5, 50]], 2, 0.25),
        ([[2, 50]], 0, 0.0),
    ],
)
class TestSolution:
    def test_calculateTax(self, brackets: List[List[int]], income: int, output: float):
        sc = Solution()
        assert (
            sc.calculateTax(
                brackets,
                income,
            )
            == output
        )
