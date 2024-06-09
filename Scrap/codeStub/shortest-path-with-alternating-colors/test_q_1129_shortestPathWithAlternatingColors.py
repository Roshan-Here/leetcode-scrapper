import pytest
from q_1129_shortestPathWithAlternatingColors import Solution


@pytest.mark.parametrize(
    "n, redEdges, blueEdges, output",
    [(3, [[0, 1], [1, 2]], [], [0, 1, -1]), (3, [[0, 1]], [[2, 1]], [0, 1, -1])],
)
class TestSolution:
    def test_shortestAlternatingPaths(
        self,
        n: int,
        redEdges: List[List[int]],
        blueEdges: List[List[int]],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.shortestAlternatingPaths(
                n,
                redEdges,
                blueEdges,
            )
            == output
        )
