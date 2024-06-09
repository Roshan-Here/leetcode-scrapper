import pytest
from q_1074_numberOfSubmatricesThatSumToTarget import Solution


@pytest.mark.parametrize(
    "matrix, target, output",
    [
        ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4),
        ([[1, -1], [-1, 1]], 0, 5),
        ([[904]], 0, 0),
    ],
)
class TestSolution:
    def test_numSubmatrixSumTarget(
        self, matrix: List[List[int]], target: int, output: int
    ):
        sc = Solution()
        assert (
            sc.numSubmatrixSumTarget(
                matrix,
                target,
            )
            == output
        )
