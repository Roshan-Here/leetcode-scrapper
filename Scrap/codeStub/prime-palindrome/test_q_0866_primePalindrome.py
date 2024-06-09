import pytest
from q_0866_primePalindrome import Solution


@pytest.mark.parametrize("n, output", [(6, 7), (8, 11), (13, 101)])
class TestSolution:
    def test_primePalindrome(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.primePalindrome(
                n,
            )
            == output
        )
