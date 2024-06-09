import pytest
from q_3159_findOccurrencesOfAnElementInAnArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int, output: List[int]
    ):
        sc = Solution()
        assert sc.occurrencesOfElement() == output
