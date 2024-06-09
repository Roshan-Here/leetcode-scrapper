import pytest
from q_1304_findNUniqueIntegersSumUpToZero import Solution


@pytest.mark.parametrize(
    "n, output", [(5, [-7, -1, 1, 3, 4]), (3, [-1, 0, 1]), (1, [0])]
)
class TestSolution:
    def test_sumZero(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.sumZero(
                n,
            )
            == output
        )
