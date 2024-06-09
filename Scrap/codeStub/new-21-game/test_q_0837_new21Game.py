import pytest
from q_0837_new21Game import Solution


@pytest.mark.parametrize(
    "n, k, maxPts, output", [(10, 1, 10, 1.0), (6, 1, 10, 0.6), (21, 17, 10, 0.73278)]
)
class TestSolution:
    def test_new21Game(self, n: int, k: int, maxPts: int, output: float):
        sc = Solution()
        assert (
            sc.new21Game(
                n,
                k,
                maxPts,
            )
            == output
        )
