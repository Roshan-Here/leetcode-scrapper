import pytest
from q_1629_slowestKey import Solution


@pytest.mark.parametrize(
    "releaseTimes, keysPressed, output",
    [([9, 29, 49, 50], "cbcd", "c"), ([12, 23, 36, 46, 62], "spuda", "a")],
)
class TestSolution:
    def test_slowestKey(self, releaseTimes: List[int], keysPressed: str, output: str):
        sc = Solution()
        assert (
            sc.slowestKey(
                releaseTimes,
                keysPressed,
            )
            == output
        )
