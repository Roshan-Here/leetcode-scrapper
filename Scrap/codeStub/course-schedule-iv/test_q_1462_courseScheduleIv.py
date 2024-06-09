import pytest
from q_1462_courseScheduleIv import Solution


@pytest.mark.parametrize(
    "numCourses, prerequisites, queries, output",
    [
        (2, [[1, 0]], [[0, 1], [1, 0]], [False, True]),
        (2, [], [[1, 0], [0, 1]], [False, False]),
        (3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]], [True, True]),
    ],
)
class TestSolution:
    def test_checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
        output: List[bool],
    ):
        sc = Solution()
        assert (
            sc.checkIfPrerequisite(
                numCourses,
                prerequisites,
                queries,
            )
            == output
        )
