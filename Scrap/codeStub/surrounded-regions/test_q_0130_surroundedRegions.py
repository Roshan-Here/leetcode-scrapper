import pytest
from q_0130_surroundedRegions import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_solve(self, board: List[List[str]], output: None):
        sc = Solution()
        assert sc.solve() == output
