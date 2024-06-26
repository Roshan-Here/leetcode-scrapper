import pytest
from q_1786_numberOfRestrictedPathsFromFirstToLastNode import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (
            5,
            [
                [1, 2, 3],
                [1, 3, 3],
                [2, 3, 1],
                [1, 4, 2],
                [5, 2, 2],
                [3, 5, 1],
                [5, 4, 10],
            ],
            3,
        ),
        (
            7,
            [
                [1, 3, 1],
                [4, 1, 2],
                [7, 3, 4],
                [2, 5, 3],
                [5, 6, 1],
                [6, 7, 2],
                [7, 5, 3],
                [2, 6, 4],
            ],
            1,
        ),
    ],
)
class TestSolution:
    def test_countRestrictedPaths(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countRestrictedPaths(
                n,
                edges,
            )
            == output
        )
