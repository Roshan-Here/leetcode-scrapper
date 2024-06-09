import pytest
from q_1839_longestSubstringOfAllVowelsInOrder import Solution


@pytest.mark.parametrize(
    "word, output",
    [("aeiaaioaaaaeiiiiouuuooaauuaeiu", 13), ("aeeeiiiioooauuuaeiou", 5), ("a", 0)],
)
class TestSolution:
    def test_longestBeautifulSubstring(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.longestBeautifulSubstring(
                word,
            )
            == output
        )
