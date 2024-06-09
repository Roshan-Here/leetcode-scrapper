import pytest
from q_0794_validTicTacToeState import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        (["O  ", "   ", "   "], False),
        (["XOX", " X ", "   "], False),
        (["XOX", "O O", "XOX"], True),
    ],
)
class TestSolution:
    def test_validTicTacToe(self, board: List[str], output: bool):
        sc = Solution()
        assert (
            sc.validTicTacToe(
                board,
            )
            == output
        )
