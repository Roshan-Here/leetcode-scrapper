import pytest
from q_2791_countPathsThatCanFormAPalindromeInATree import Solution


@pytest.mark.parametrize(
    "parent, s, output",
    [([-1, 0, 0, 1, 1, 2], "acaabc", 8), ([-1, 0, 0, 0, 0], "aaaaa", 10)],
)
class TestSolution:
    def test_countPalindromePaths(self, parent: List[int], s: str, output: int):
        sc = Solution()
        assert (
            sc.countPalindromePaths(
                parent,
                s,
            )
            == output
        )
