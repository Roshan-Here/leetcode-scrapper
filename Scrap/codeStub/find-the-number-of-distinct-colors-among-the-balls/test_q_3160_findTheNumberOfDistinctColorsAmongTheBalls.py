import pytest
from q_3160_findTheNumberOfDistinctColorsAmongTheBalls import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_queryResults(
        self, limit: int, queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert sc.queryResults() == output
