import pytest
from q_0935_knightDialer import Solution


@pytest.mark.parametrize("n, output", [(1, 10), (2, 20), (3131, 136006598)])
class TestSolution:
    def test_knightDialer(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.knightDialer(
                n,
            )
            == output
        )
