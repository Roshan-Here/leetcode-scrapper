import pytest
from q_2188_minimumTimeToFinishTheRace import Solution


@pytest.mark.parametrize(
    "tires, changeTime, numLaps, output",
    [([[2, 3], [3, 4]], 5, 4, 21), ([[1, 10], [2, 2], [3, 4]], 6, 5, 25)],
)
class TestSolution:
    def test_minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minimumFinishTime(
                tires,
                changeTime,
                numLaps,
            )
            == output
        )
