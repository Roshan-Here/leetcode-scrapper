import pytest
from q_3084_countSubstringsStartingAndEndingWithGivenCharacter import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_countSubstrings(self, s: str, c: str, output: int):
        sc = Solution()
        assert sc.countSubstrings() == output
