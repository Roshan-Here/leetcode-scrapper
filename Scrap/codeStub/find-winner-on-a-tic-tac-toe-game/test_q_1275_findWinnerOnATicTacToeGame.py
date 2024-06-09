import pytest
from q_1275_findWinnerOnATicTacToeGame import Solution


@pytest.mark.parametrize(
    "moves, output",
    [
        ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
        ([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], "B"),
        (
            [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]],
            "Draw",
        ),
    ],
)
class TestSolution:
    def test_tictactoe(self, moves: List[List[int]], output: str):
        sc = Solution()
        assert (
            sc.tictactoe(
                moves,
            )
            == output
        )
