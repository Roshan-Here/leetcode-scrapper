import pytest
from q_2218_maximumValueOfKCoinsFromPiles import Solution


@pytest.mark.parametrize(
    "piles, k, output",
    [
        ([[1, 100, 3], [7, 8, 9]], 2, 101),
        ([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7, 706),
    ],
)
class TestSolution:
    def test_maxValueOfCoins(self, piles: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxValueOfCoins(
                piles,
                k,
            )
            == output
        )
