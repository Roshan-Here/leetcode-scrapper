import pytest
from q_0140_wordBreakIi import Solution


@pytest.mark.parametrize(
    "s, wordDict, output",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cats and dog", "cat sand dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ],
)
class TestSolution:
    def test_wordBreak(self, s: str, wordDict: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.wordBreak(
                s,
                wordDict,
            )
            == output
        )
