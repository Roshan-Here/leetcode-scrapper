import pytest
from q_2491_dividePlayersIntoTeamsOfEqualSkill import Solution


@pytest.mark.parametrize(
    "skill, output", [([3, 2, 5, 1, 3, 4], 22), ([3, 4], 12), ([1, 1, 2, 3], -1)]
)
class TestSolution:
    def test_dividePlayers(self, skill: List[int], output: int):
        sc = Solution()
        assert (
            sc.dividePlayers(
                skill,
            )
            == output
        )
