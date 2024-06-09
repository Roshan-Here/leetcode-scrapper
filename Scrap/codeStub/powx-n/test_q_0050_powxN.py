import pytest
from q_0050_powxN import Solution


@pytest.mark.parametrize(
    "x, n, output", [(2.0, 10, 1024.0), (2.1, 3, 9.261), (2.0, -2, 0.25)]
)
class TestSolution:
    def test_myPow(self, x: float, n: int, output: float):
        sc = Solution()
        assert (
            sc.myPow(
                x,
                n,
            )
            == output
        )
