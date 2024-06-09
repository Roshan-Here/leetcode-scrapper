import pytest
from q_0804_uniqueMorseCodeWords import Solution


@pytest.mark.parametrize(
    "words, output", [(["gin", "zen", "gig", "msg"], 2), (["a"], 1)]
)
class TestSolution:
    def test_uniqueMorseRepresentations(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.uniqueMorseRepresentations(
                words,
            )
            == output
        )
