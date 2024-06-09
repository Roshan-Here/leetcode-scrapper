import pytest
from q_2564_substringXorQueries import Solution


@pytest.mark.parametrize(
    "s, queries, output",
    [
        ("101101", [[0, 5], [1, 2]], [[0, 2], [2, 3]]),
        ("0101", [[12, 8]], [[-1, -1]]),
        ("1", [[4, 5]], [[0, 0]]),
    ],
)
class TestSolution:
    def test_substringXorQueries(
        self, s: str, queries: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.substringXorQueries(
                s,
                queries,
            )
            == output
        )
