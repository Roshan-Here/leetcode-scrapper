import pytest
from q_2937_makeThreeStringsEqual import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findMinimumOperations(self, s1: str, s2: str, s3: str, output: int):
        sc = Solution()
        assert sc.findMinimumOperations() == output
