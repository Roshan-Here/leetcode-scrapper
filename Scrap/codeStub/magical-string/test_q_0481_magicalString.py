import pytest
from q_0481_magicalString import Solution


@pytest.mark.parametrize("n, output", [(6, 3), (1, 1)])
class TestSolution:
    def test_magicalString(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.magicalString(
                n,
            )
            == output
        )
