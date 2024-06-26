import pytest
from q_2245_maximumTrailingZerosInACorneredPath import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                [23, 17, 15, 3, 20],
                [8, 1, 20, 27, 11],
                [9, 4, 6, 2, 21],
                [40, 9, 1, 10, 6],
                [22, 7, 4, 5, 3],
            ],
            3,
        ),
        ([[4, 3, 2], [7, 6, 1], [8, 8, 8]], 0),
    ],
)
class TestSolution:
    def test_maxTrailingZeros(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxTrailingZeros(
                grid,
            )
            == output
        )
