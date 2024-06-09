import pytest
from q_2685_countTheNumberOfCompleteComponents import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3),
        (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1),
    ],
)
class TestSolution:
    def test_countCompleteComponents(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countCompleteComponents(
                n,
                edges,
            )
            == output
        )
