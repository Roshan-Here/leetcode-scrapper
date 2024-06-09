import pytest
from q_3121_countTheNumberOfSpecialCharactersIi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfSpecialChars(self, word: str, output: int):
        sc = Solution()
        assert sc.numberOfSpecialChars() == output
