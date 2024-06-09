import pytest
from q_1627_graphConnectivityWithThreshold import Solution


@pytest.mark.parametrize(
    "n, threshold, queries, output",
    [
        (6, 2, [[1, 4], [2, 5], [3, 6]], [False, False, True]),
        (
            6,
            0,
            [[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]],
            [True, True, True, True, True],
        ),
        (
            5,
            1,
            [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]],
            [False, False, False, False, False],
        ),
    ],
)
class TestSolution:
    def test_areConnected(
        self, n: int, threshold: int, queries: List[List[int]], output: List[bool]
    ):
        sc = Solution()
        assert (
            sc.areConnected(
                n,
                threshold,
                queries,
            )
            == output
        )
