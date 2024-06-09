import pytest
from q_1240_tilingARectangleWithTheFewestSquares import Solution


@pytest.mark.parametrize("n, m, output", [(2, 3, 3), (5, 8, 5), (11, 13, 6)])
class TestSolution:
    def test_tilingRectangle(self, n: int, m: int, output: int):
        sc = Solution()
        assert (
            sc.tilingRectangle(
                n,
                m,
            )
            == output
        )
