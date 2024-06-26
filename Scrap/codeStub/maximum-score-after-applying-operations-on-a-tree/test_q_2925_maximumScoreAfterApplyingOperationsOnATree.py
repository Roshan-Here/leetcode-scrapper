import pytest
from q_2925_maximumScoreAfterApplyingOperationsOnATree import Solution


@pytest.mark.parametrize(
    "edges, values, output",
    [
        ([[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], [5, 2, 5, 2, 1, 1], 11),
        ([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [20, 10, 9, 7, 4, 3, 5], 40),
    ],
)
class TestSolution:
    def test_maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maximumScoreAfterOperations(
                edges,
                values,
            )
            == output
        )
