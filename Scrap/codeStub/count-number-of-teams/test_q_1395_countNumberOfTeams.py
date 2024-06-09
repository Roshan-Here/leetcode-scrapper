import pytest
from q_1395_countNumberOfTeams import Solution


@pytest.mark.parametrize(
    "rating, output", [([2, 5, 3, 4, 1], 3), ([2, 1, 3], 0), ([1, 2, 3, 4], 4)]
)
class TestSolution:
    def test_numTeams(self, rating: List[int], output: int):
        sc = Solution()
        assert (
            sc.numTeams(
                rating,
            )
            == output
        )
