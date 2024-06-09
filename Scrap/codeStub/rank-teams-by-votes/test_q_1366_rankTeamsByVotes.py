import pytest
from q_1366_rankTeamsByVotes import Solution


@pytest.mark.parametrize(
    "votes, output",
    [
        (["ABC", "ACB", "ABC", "ACB", "ACB"], "ACB"),
        (["WXYZ", "XYZW"], "XWYZ"),
        (["ZMNAGUEDSJYLBOPHRQICWFXTVK"], "ZMNAGUEDSJYLBOPHRQICWFXTVK"),
    ],
)
class TestSolution:
    def test_rankTeams(self, votes: List[str], output: str):
        sc = Solution()
        assert (
            sc.rankTeams(
                votes,
            )
            == output
        )
