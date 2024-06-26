import pytest
from q_1721_swappingNodesInALinkedList import Solution


@pytest.mark.parametrize(
    "head, k, output",
    [
        ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
        ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
    ],
)
class TestSolution:
    def test_swapNodes(
        self, head: Optional[ListNode], k: int, output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.swapNodes(
                head,
                k,
            )
            == output
        )
