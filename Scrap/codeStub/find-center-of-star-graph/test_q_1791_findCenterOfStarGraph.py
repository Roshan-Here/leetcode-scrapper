import pytest
from q_1791_findCenterOfStarGraph import Solution


@pytest.mark.parametrize(
    "edges, output",
    [([[1, 2], [2, 3], [4, 2]], 2), ([[1, 2], [5, 1], [1, 3], [1, 4]], 1)],
)
class TestSolution:
    def test_findCenter(self, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findCenter(
                edges,
            )
            == output
        )
