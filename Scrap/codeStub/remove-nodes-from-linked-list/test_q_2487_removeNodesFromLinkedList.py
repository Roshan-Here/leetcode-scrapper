import pytest
from q_2487_removeNodesFromLinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([5, 2, 13, 3, 8], [13, 8]), ([1, 1, 1, 1], [1, 1, 1, 1])]
)
class TestSolution:
    def test_removeNodes(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.removeNodes(
                head,
            )
            == output
        )
