import pytest
from q_0151_reverseWordsInAString import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ],
)
class TestSolution:
    def test_reverseWords(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.reverseWords(
                s,
            )
            == output
        )
