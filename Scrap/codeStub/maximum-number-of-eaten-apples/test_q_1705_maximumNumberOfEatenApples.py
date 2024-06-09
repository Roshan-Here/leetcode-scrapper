import pytest
from q_1705_maximumNumberOfEatenApples import Solution


@pytest.mark.parametrize(
    "apples, days, output",
    [
        ([1, 2, 3, 5, 2], [3, 2, 1, 4, 2], 7),
        ([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2], 5),
    ],
)
class TestSolution:
    def test_eatenApples(self, apples: List[int], days: List[int], output: int):
        sc = Solution()
        assert (
            sc.eatenApples(
                apples,
                days,
            )
            == output
        )
