import pytest
from q_2901_longestUnequalAdjacentGroupsSubsequenceIi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int], output: List[str]
    ):
        sc = Solution()
        assert sc.getWordsInLongestSubsequence() == output
