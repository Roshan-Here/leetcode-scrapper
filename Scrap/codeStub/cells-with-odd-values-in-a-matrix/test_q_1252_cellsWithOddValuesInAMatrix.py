import pytest
from q_1252_cellsWithOddValuesInAMatrix import Solution


@pytest.mark.parametrize(
    "m, n, indices, output", [(2, 3, [[0, 1], [1, 1]], 6), (2, 2, [[1, 1], [0, 0]], 0)]
)
class TestSolution:
    def test_oddCells(self, m: int, n: int, indices: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.oddCells(
                m,
                n,
                indices,
            )
            == output
        )
