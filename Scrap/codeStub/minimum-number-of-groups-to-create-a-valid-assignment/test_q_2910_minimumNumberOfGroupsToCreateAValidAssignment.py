import pytest
from q_2910_minimumNumberOfGroupsToCreateAValidAssignment import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minGroupsForValidAssignment(self, balls: List[int], output: int):
        sc = Solution()
        assert sc.minGroupsForValidAssignment() == output
