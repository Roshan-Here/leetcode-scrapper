import pytest
from q_1006_clumsyFactorial import Solution


@pytest.mark.parametrize("n, output", [(4, 7), (10, 12)])
class TestSolution:
    def test_clumsy(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.clumsy(
                n,
            )
            == output
        )
