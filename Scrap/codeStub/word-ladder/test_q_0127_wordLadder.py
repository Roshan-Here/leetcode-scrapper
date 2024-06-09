import pytest
from q_0127_wordLadder import Solution


@pytest.mark.parametrize(
    "beginWord, endWord, wordList, output",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
)
class TestSolution:
    def test_ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str], output: int
    ):
        sc = Solution()
        assert (
            sc.ladderLength(
                beginWord,
                endWord,
                wordList,
            )
            == output
        )
