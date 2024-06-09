import pytest
from q_1961_checkIfStringIsAPrefixOfArray import Solution


@pytest.mark.parametrize(
    "s, words, output",
    [
        ("iloveleetcode", ["i", "love", "leetcode", "apples"], True),
        ("iloveleetcode", ["apples", "i", "love", "leetcode"], False),
    ],
)
class TestSolution:
    def test_isPrefixString(self, s: str, words: List[str], output: bool):
        sc = Solution()
        assert (
            sc.isPrefixString(
                s,
                words,
            )
            == output
        )
