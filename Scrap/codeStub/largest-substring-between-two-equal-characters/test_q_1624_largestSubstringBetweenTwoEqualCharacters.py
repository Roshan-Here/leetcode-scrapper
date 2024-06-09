import pytest
from q_1624_largestSubstringBetweenTwoEqualCharacters import Solution


@pytest.mark.parametrize("s, output", [("aa", 0), ("abca", 2), ("cbzxy", -1)])
class TestSolution:
    def test_maxLengthBetweenEqualCharacters(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxLengthBetweenEqualCharacters(
                s,
            )
            == output
        )
