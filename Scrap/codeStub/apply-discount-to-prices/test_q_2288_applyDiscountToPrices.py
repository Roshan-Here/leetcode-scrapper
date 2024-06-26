import pytest
from q_2288_applyDiscountToPrices import Solution


@pytest.mark.parametrize(
    "sentence, discount, output",
    [
        (
            "there are $1 $2 and 5$ candies in the shop",
            50,
            "there are $0.50 $1.00 and 5$ candies in the shop",
        ),
        ("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100, "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"),
    ],
)
class TestSolution:
    def test_discountPrices(self, sentence: str, discount: int, output: str):
        sc = Solution()
        assert (
            sc.discountPrices(
                sentence,
                discount,
            )
            == output
        )
