import pytest
from q_2481_minimumCutsToDivideACircle import Solution


@pytest.mark.parametrize("n, output", [(4, 2), (3, 3)])
class TestSolution:
    def test_numberOfCuts(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfCuts(
                n,
            )
            == output
        )
