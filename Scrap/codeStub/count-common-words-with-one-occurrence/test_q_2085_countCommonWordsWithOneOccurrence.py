import pytest
from q_2085_countCommonWordsWithOneOccurrence import Solution


@pytest.mark.parametrize(
    "words1, words2, output",
    [
        (["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"], 2),
        (["b", "bb", "bbb"], ["a", "aa", "aaa"], 0),
        (["a", "ab"], ["a", "a", "a", "ab"], 1),
    ],
)
class TestSolution:
    def test_countWords(self, words1: List[str], words2: List[str], output: int):
        sc = Solution()
        assert (
            sc.countWords(
                words1,
                words2,
            )
            == output
        )
