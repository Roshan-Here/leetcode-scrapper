import pytest
from q_1638_countSubstringsThatDifferByOneCharacter import Solution


@pytest.mark.parametrize("s, t, output", [("aba", "baba", 6), ("ab", "bb", 3)])
class TestSolution:
    def test_countSubstrings(self, s: str, t: str, output: int):
        sc = Solution()
        assert (
            sc.countSubstrings(
                s,
                t,
            )
            == output
        )
