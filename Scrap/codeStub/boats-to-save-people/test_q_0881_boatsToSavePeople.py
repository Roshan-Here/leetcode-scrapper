import pytest
from q_0881_boatsToSavePeople import Solution


@pytest.mark.parametrize(
    "people, limit, output",
    [([1, 2], 3, 1), ([3, 2, 2, 1], 3, 3), ([3, 5, 3, 4], 5, 4)],
)
class TestSolution:
    def test_numRescueBoats(self, people: List[int], limit: int, output: int):
        sc = Solution()
        assert (
            sc.numRescueBoats(
                people,
                limit,
            )
            == output
        )
