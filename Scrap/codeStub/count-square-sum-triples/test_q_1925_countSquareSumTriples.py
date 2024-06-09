import pytest
from q_1925_countSquareSumTriples import Solution


@pytest.mark.parametrize("n, output", [(5, 2), (10, 4)])
class TestSolution:
    def test_countTriples(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countTriples(
                n,
            )
            == output
        )
