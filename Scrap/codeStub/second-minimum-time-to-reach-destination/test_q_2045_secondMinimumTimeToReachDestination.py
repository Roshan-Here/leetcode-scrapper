import pytest
from q_2045_secondMinimumTimeToReachDestination import Solution


@pytest.mark.parametrize(
    "n, edges, time, change, output",
    [(5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5, 13), (2, [[1, 2]], 3, 2, 11)],
)
class TestSolution:
    def test_secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int, output: int
    ):
        sc = Solution()
        assert (
            sc.secondMinimum(
                n,
                edges,
                time,
                change,
            )
            == output
        )
