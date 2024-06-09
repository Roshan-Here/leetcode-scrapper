import pytest
from q_1665_minimumInitialEnergyToFinishTasks import Solution


@pytest.mark.parametrize(
    "tasks, output",
    [
        ([[1, 2], [2, 4], [4, 8]], 8),
        ([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], 32),
        ([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], 27),
    ],
)
class TestSolution:
    def test_minimumEffort(self, tasks: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumEffort(
                tasks,
            )
            == output
        )
