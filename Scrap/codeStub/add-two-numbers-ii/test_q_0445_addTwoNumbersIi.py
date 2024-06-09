import pytest
from q_0445_addTwoNumbersIi import Solution


@pytest.mark.parametrize(
    "l1, l2, output",
    [
        ([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
        ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
        ([0], [0], [0]),
    ],
)
class TestSolution:
    def test_addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.addTwoNumbers(
                l1,
                l2,
            )
            == output
        )
