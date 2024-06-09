import pytest
from q_3035_maximumPalindromesAfterOperations import Solution


@pytest.mark.parametrize(
    "words, output",
    [(["abbb", "ba", "aa"], 3), (["abc", "ab"], 2), (["cd", "ef", "a"], 1)],
)
class TestSolution:
    def test_maxPalindromesAfterOperations(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.maxPalindromesAfterOperations(
                words,
            )
            == output
        )
