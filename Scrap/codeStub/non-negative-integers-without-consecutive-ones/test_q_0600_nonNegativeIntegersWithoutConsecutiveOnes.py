import pytest
from q_0600_nonNegativeIntegersWithoutConsecutiveOnes import Solution


@pytest.mark.parametrize("n, output", [(5, 5), (1, 2), (2, 3)])
class TestSolution:
    def test_findIntegers(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.findIntegers(
                n,
            )
            == output
        )
