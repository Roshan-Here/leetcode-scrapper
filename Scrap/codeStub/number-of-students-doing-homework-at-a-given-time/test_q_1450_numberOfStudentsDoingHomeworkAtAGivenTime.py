import pytest
from q_1450_numberOfStudentsDoingHomeworkAtAGivenTime import Solution


@pytest.mark.parametrize(
    "startTime, endTime, queryTime, output",
    [([1, 2, 3], [3, 2, 7], 4, 1), ([4], [4], 4, 1)],
)
class TestSolution:
    def test_busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int, output: int
    ):
        sc = Solution()
        assert (
            sc.busyStudent(
                startTime,
                endTime,
                queryTime,
            )
            == output
        )
