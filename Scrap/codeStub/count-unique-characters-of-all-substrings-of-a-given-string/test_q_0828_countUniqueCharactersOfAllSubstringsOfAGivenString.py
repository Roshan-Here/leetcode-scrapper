import pytest
from q_0828_countUniqueCharactersOfAllSubstringsOfAGivenString import Solution


@pytest.mark.parametrize("s, output", [("ABC", 10), ("ABA", 8), ("LEETCODE", 92)])
class TestSolution:
    def test_uniqueLetterString(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.uniqueLetterString(
                s,
            )
            == output
        )
