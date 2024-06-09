import pytest
from q_0054_spiralMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ],
)
class TestSolution:
    def test_spiralOrder(self, matrix: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.spiralOrder(
                matrix,
            )
            == output
        )
