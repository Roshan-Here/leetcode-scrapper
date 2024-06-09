import pytest
from q_3093_longestCommonSuffixQueries import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str], output: List[int]
    ):
        sc = Solution()
        assert sc.stringIndices() == output
