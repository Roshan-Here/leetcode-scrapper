import pytest
from q_2258_escapeTheSpreadingFire import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                [0, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 2, 1, 0],
                [0, 2, 0, 0, 1, 2, 0],
                [0, 0, 2, 2, 2, 0, 2],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            3,
        ),
        ([[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]], -1),
        ([[0, 0, 0], [2, 2, 0], [1, 2, 0]], 1000000000),
    ],
)
class TestSolution:
    def test_maximumMinutes(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumMinutes(
                grid,
            )
            == output
        )
