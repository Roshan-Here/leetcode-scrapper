import pytest
from q_2545_sortTheStudentsByTheirKthScore import Solution


@pytest.mark.parametrize(
    "score, k, output",
    [
        (
            [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]],
            2,
            [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]],
        ),
        ([[3, 4], [5, 6]], 0, [[5, 6], [3, 4]]),
    ],
)
class TestSolution:
    def test_sortTheStudents(
        self, score: List[List[int]], k: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.sortTheStudents(
                score,
                k,
            )
            == output
        )
