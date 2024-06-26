import pytest
from q_1604_alertUsingSameKeyCardThreeOrMoreTimesInAOneHourPeriod import Solution


@pytest.mark.parametrize(
    "keyName, keyTime, output",
    [
        (
            ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
            ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"],
            ["daniel"],
        ),
        (
            ["alice", "alice", "alice", "bob", "bob", "bob", "bob"],
            ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"],
            ["bob"],
        ),
    ],
)
class TestSolution:
    def test_alertNames(
        self, keyName: List[str], keyTime: List[str], output: List[str]
    ):
        sc = Solution()
        assert (
            sc.alertNames(
                keyName,
                keyTime,
            )
            == output
        )
