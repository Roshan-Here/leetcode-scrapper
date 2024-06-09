import pytest
from q_2047_numberOfValidWordsInASentence import Solution


@pytest.mark.parametrize(
    "sentence, output",
    [
        ("cat and  dog", 3),
        ("!this  1-s b8d!", 0),
        ("alice and  bob are playing stone-game10", 5),
    ],
)
class TestSolution:
    def test_countValidWords(self, sentence: str, output: int):
        sc = Solution()
        assert (
            sc.countValidWords(
                sentence,
            )
            == output
        )
