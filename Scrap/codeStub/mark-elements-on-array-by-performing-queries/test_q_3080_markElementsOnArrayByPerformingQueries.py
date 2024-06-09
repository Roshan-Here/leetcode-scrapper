import pytest
from q_3080_markElementsOnArrayByPerformingQueries import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_unmarkedSumArray(
        self, nums: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert sc.unmarkedSumArray() == output
