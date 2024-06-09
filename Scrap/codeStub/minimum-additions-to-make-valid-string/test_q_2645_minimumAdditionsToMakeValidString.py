import pytest
from q_2645_minimumAdditionsToMakeValidString import Solution


@pytest.mark.parametrize("word, output", [("b", 2), ("aaa", 6), ("abc", 0)])
class TestSolution:
    def test_addMinimum(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.addMinimum(
                word,
            )
            == output
        )
