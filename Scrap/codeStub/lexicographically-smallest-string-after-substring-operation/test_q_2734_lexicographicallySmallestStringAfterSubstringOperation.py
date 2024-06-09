import pytest
from q_2734_lexicographicallySmallestStringAfterSubstringOperation import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_smallestString(self, s: str, output: str):
        sc = Solution()
        assert sc.smallestString() == output
