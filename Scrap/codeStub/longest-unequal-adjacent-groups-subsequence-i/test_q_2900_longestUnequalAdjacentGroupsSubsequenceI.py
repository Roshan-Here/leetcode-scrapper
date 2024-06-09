import pytest
from q_2900_longestUnequalAdjacentGroupsSubsequenceI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_getLongestSubsequence(
        self, words: List[str], groups: List[int], output: List[str]
    ):
        sc = Solution()
        assert sc.getLongestSubsequence() == output
