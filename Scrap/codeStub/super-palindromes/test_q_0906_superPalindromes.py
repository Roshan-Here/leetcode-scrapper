import pytest
from q_0906_superPalindromes import Solution


@pytest.mark.parametrize("left, right, output", [("4", "1000", 4), ("1", "2", 1)])
class TestSolution:
    def test_superpalindromesInRange(self, left: str, right: str, output: int):
        sc = Solution()
        assert (
            sc.superpalindromesInRange(
                left,
                right,
            )
            == output
        )
