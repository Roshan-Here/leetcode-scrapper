import pytest
from q_0290_wordPattern import Solution


@pytest.mark.parametrize(
    "pattern, s, output",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ],
)
class TestSolution:
    def test_wordPattern(self, pattern: str, s: str, output: bool):
        sc = Solution()
        assert (
            sc.wordPattern(
                pattern,
                s,
            )
            == output
        )
