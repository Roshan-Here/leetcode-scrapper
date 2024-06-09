import pytest
from q_3120_countTheNumberOfSpecialCharactersI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfSpecialChars(self, word: str, output: int):
        sc = Solution()
        assert sc.numberOfSpecialChars() == output
