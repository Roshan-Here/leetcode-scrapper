import pytest
from q_2826_sortingThreeGroups import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.minimumOperations() == output
