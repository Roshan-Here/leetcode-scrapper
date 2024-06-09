import pytest
from q_2660_determineTheWinnerOfABowlingGame import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_isWinner(self, player1: List[int], player2: List[int], output: int):
        sc = Solution()
        assert sc.isWinner() == output
