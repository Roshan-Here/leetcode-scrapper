import pytest
from q_3106_lexicographicallySmallestStringAfterOperationsWithConstraint import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_getSmallestString(self, s: str, k: int, output: str):
        sc = Solution()
        assert sc.getSmallestString() == output
