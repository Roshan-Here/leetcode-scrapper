import pytest
from q_1926_nearestExitFromEntranceInMaze import Solution


@pytest.mark.parametrize(
    "maze, entrance, output",
    [
        ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2], 1),
        ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2),
        ([[".", "+"]], [0, 0], -1),
    ],
)
class TestSolution:
    def test_nearestExit(self, maze: List[List[str]], entrance: List[int], output: int):
        sc = Solution()
        assert (
            sc.nearestExit(
                maze,
                entrance,
            )
            == output
        )
