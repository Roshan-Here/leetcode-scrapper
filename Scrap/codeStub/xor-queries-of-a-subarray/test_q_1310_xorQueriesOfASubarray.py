import pytest
from q_1310_xorQueriesOfASubarray import Solution


@pytest.mark.parametrize(
    "arr, queries, output",
    [
        ([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]], [2, 7, 14, 8]),
        ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]], [8, 0, 4, 4]),
    ],
)
class TestSolution:
    def test_xorQueries(
        self, arr: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.xorQueries(
                arr,
                queries,
            )
            == output
        )
