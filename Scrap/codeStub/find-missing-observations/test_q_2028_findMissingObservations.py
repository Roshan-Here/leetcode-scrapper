import pytest
from q_2028_findMissingObservations import Solution


@pytest.mark.parametrize(
    "rolls, mean, n, output",
    [
        ([3, 2, 4, 3], 4, 2, [6, 6]),
        ([1, 5, 6], 3, 4, [2, 3, 2, 2]),
        ([1, 2, 3, 4], 6, 4, []),
    ],
)
class TestSolution:
    def test_missingRolls(self, rolls: List[int], mean: int, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.missingRolls(
                rolls,
                mean,
                n,
            )
            == output
        )
