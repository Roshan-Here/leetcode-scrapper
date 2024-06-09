import pytest
from q_1553_minimumNumberOfDaysToEatNOranges import Solution


@pytest.mark.parametrize("n, output", [(10, 4), (6, 3)])
class TestSolution:
    def test_minDays(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.minDays(
                n,
            )
            == output
        )
