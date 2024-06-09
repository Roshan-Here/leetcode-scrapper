import pytest
from q_2711_differenceOfNumberOfDistinctValuesOnDiagonals import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_differenceOfDistinctValues(
        self, grid: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert sc.differenceOfDistinctValues() == output
