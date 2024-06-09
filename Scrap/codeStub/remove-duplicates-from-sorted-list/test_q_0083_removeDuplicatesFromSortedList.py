import pytest
from q_0083_removeDuplicatesFromSortedList import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 1, 2], [1, 2]), ([1, 1, 2, 3, 3], [1, 2, 3])]
)
class TestSolution:
    def test_deleteDuplicates(
        self, head: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.deleteDuplicates(
                head,
            )
            == output
        )
