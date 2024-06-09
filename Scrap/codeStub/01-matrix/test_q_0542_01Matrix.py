import pytest
from q_0542_01Matrix import Solution


@pytest.mark.parametrize(
    "mat, output",
    [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
    ],
)
class TestSolution:
    def test_updateMatrix(self, mat: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.updateMatrix(
                mat,
            )
            == output
        )
