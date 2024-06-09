import pytest
from q_1579_removeMaxNumberOfEdgesToKeepGraphFullyTraversable import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]], 2),
        (4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]], 0),
        (4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]], -1),
    ],
)
class TestSolution:
    def test_maxNumEdgesToRemove(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxNumEdgesToRemove(
                n,
                edges,
            )
            == output
        )
