import pytest
from q_0363_maxSumOfRectangleNoLargerThanK import Solution


@pytest.mark.parametrize(
    "matrix, k, output", [([[1, 0, 1], [0, -2, 3]], 2, 2), ([[2, 2, -1]], 3, 3)]
)
class TestSolution:
    def test_maxSumSubmatrix(self, matrix: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxSumSubmatrix(
                matrix,
                k,
            )
            == output
        )
