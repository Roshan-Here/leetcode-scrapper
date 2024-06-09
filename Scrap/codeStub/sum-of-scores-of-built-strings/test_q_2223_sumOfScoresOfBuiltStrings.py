import pytest
from q_2223_sumOfScoresOfBuiltStrings import Solution


@pytest.mark.parametrize("s, output", [("babab", 9), ("azbazbzaz", 14)])
class TestSolution:
    def test_sumScores(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.sumScores(
                s,
            )
            == output
        )
