import pytest
from q_3112_minimumTimeToVisitDisappearingNodes import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int], output: List[int]
    ):
        sc = Solution()
        assert sc.minimumTime() == output
