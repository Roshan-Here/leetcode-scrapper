import pytest
from q_1371_findTheLongestSubstringContainingVowelsInEvenCounts import Solution


@pytest.mark.parametrize(
    "s, output", [("eleetminicoworoep", 13), ("leetcodeisgreat", 5), ("bcbcbc", 6)]
)
class TestSolution:
    def test_findTheLongestSubstring(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.findTheLongestSubstring(
                s,
            )
            == output
        )
