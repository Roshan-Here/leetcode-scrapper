import pytest
from q_0086_partitionList import Solution


@pytest.mark.parametrize(
    "head, x, output",
    [([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]), ([2, 1], 2, [1, 2])],
)
class TestSolution:
    def test_partition(
        self, head: Optional[ListNode], x: int, output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.partition(
                head,
                x,
            )
            == output
        )
