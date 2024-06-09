import pytest
from q_1697_checkingExistenceOfEdgeLengthLimitedPaths import Solution


@pytest.mark.parametrize(
    "n, edgeList, queries, output",
    [
        (
            3,
            [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
            [[0, 1, 2], [0, 2, 5]],
            [False, True],
        ),
        (
            5,
            [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
            [[0, 4, 14], [1, 4, 13]],
            [True, False],
        ),
    ],
)
class TestSolution:
    def test_distanceLimitedPathsExist(
        self,
        n: int,
        edgeList: List[List[int]],
        queries: List[List[int]],
        output: List[bool],
    ):
        sc = Solution()
        assert (
            sc.distanceLimitedPathsExist(
                n,
                edgeList,
                queries,
            )
            == output
        )
