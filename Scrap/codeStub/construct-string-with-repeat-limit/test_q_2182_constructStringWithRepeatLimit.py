import pytest
from q_2182_constructStringWithRepeatLimit import Solution


@pytest.mark.parametrize(
    "s, repeatLimit, output", [("cczazcc", 3, "zzcccac"), ("aababab", 2, "bbabaa")]
)
class TestSolution:
    def test_repeatLimitedString(self, s: str, repeatLimit: int, output: str):
        sc = Solution()
        assert (
            sc.repeatLimitedString(
                s,
                repeatLimit,
            )
            == output
        )
