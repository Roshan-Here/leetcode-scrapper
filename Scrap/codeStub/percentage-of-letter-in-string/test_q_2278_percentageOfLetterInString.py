import pytest
from q_2278_percentageOfLetterInString import Solution


@pytest.mark.parametrize("s, letter, output", [("foobar", "o", 33), ("jjjj", "k", 0)])
class TestSolution:
    def test_percentageLetter(self, s: str, letter: str, output: int):
        sc = Solution()
        assert (
            sc.percentageLetter(
                s,
                letter,
            )
            == output
        )
