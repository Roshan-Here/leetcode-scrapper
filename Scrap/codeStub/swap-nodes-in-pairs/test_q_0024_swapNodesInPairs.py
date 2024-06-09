import pytest
from q_0024_swapNodesInPairs import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 2, 3, 4], [2, 1, 4, 3]), ([], []), ([1], [1])]
)
class TestSolution:
    def test_swapPairs(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.swapPairs(
                head,
            )
            == output
        )
