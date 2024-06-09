import pytest
from q_0204_countPrimes import Solution


@pytest.mark.parametrize("n, output", [(10, 4), (0, 0), (1, 0)])
class TestSolution:
    def test_countPrimes(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countPrimes(
                n,
            )
            == output
        )
