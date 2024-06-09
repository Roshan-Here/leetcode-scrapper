import pytest
from q_0799_champagneTower import Solution


@pytest.mark.parametrize(
    "poured, query_row, query_glass, output",
    [(1, 1, 1, 0.0), (2, 1, 1, 0.5), (100000009, 33, 17, 1.0)],
)
class TestSolution:
    def test_champagneTower(
        self, poured: int, query_row: int, query_glass: int, output: float
    ):
        sc = Solution()
        assert (
            sc.champagneTower(
                poured,
                query_row,
                query_glass,
            )
            == output
        )
