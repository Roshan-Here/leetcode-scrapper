import pytest
from q_0070_climbingStairs import Solution


@pytest.mark.parametrize("n, output", [(2, 2), (3, 3)])
class TestSolution:
    def test_climbStairs(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.climbStairs(
                n,
            )
            == output
        )
