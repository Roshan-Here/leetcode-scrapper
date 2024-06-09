import pytest
from q_2409_countDaysSpentTogether import Solution


@pytest.mark.parametrize(
    "arriveAlice, leaveAlice, arriveBob, leaveBob, output",
    [("08-15", "08-18", "08-16", "08-19", 3), ("10-01", "10-31", "11-01", "12-31", 0)],
)
class TestSolution:
    def test_countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.countDaysTogether(
                arriveAlice,
                leaveAlice,
                arriveBob,
                leaveBob,
            )
            == output
        )
