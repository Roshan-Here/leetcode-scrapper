import pytest
from q_2973_findNumberOfCoinsToPlaceInTreeNodes import Solution


@pytest.mark.parametrize(
    "edges, cost, output",
    [
        (
            [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],
            [1, 2, 3, 4, 5, 6],
            [120, 1, 1, 1, 1, 1],
        ),
        (
            [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]],
            [1, 4, 2, 3, 5, 7, 8, -4, 2],
            [280, 140, 32, 1, 1, 1, 1, 1, 1],
        ),
        ([[0, 1], [0, 2]], [1, 2, -2], [0, 1, 1]),
    ],
)
class TestSolution:
    def test_placedCoins(
        self, edges: List[List[int]], cost: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.placedCoins(
                edges,
                cost,
            )
            == output
        )
