import pytest
from q_0059_spiralMatrixIi import Solution


@pytest.mark.parametrize(
    "n, output", [(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]), (1, [[1]])]
)
class TestSolution:
    def test_generateMatrix(self, n: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.generateMatrix(
                n,
            )
            == output
        )
