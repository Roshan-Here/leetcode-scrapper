import pytest
from q_0234_palindromeLinkedList import Solution


@pytest.mark.parametrize("head, output", [([1, 2, 2, 1], True), ([1, 2], False)])
class TestSolution:
    def test_isPalindrome(self, head: Optional[ListNode], output: bool):
        sc = Solution()
        assert (
            sc.isPalindrome(
                head,
            )
            == output
        )
