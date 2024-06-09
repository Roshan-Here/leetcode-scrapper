import pytest
from q_2058_findTheMinimumAndMaximumNumberOfNodesBetweenCriticalPoints import Solution


@pytest.mark.parametrize(
    "head, output",
    [
        ([3, 1], [-1, -1]),
        ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
        ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
    ],
)
class TestSolution:
    def test_nodesBetweenCriticalPoints(
        self, head: Optional[ListNode], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.nodesBetweenCriticalPoints(
                head,
            )
            == output
        )
