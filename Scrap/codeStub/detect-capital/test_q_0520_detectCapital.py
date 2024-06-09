import pytest
from q_0520_detectCapital import Solution


@pytest.mark.parametrize("word, output", [("USA", True), ("FlaG", False)])
class TestSolution:
    def test_detectCapitalUse(self, word: str, output: bool):
        sc = Solution()
        assert (
            sc.detectCapitalUse(
                word,
            )
            == output
        )
