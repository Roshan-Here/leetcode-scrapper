import pytest
from q_1832_checkIfTheSentenceIsPangram import Solution


@pytest.mark.parametrize(
    "sentence, output",
    [("thequickbrownfoxjumpsoverthelazydog", True), ("leetcode", False)],
)
class TestSolution:
    def test_checkIfPangram(self, sentence: str, output: bool):
        sc = Solution()
        assert (
            sc.checkIfPangram(
                sentence,
            )
            == output
        )
