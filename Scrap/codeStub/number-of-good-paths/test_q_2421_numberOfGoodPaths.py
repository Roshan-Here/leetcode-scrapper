import pytest
from q_2421_numberOfGoodPaths import Solution


@pytest.mark.parametrize(
    "vals, edges, output",
    [
        ([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]], 6),
        ([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]], 7),
        ([1], [], 1),
    ],
)
class TestSolution:
    def test_numberOfGoodPaths(
        self, vals: List[int], edges: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.numberOfGoodPaths(
                vals,
                edges,
            )
            == output
        )
