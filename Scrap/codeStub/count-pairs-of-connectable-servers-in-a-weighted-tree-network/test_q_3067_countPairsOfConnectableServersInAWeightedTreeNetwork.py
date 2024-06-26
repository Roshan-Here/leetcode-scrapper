import pytest
from q_3067_countPairsOfConnectableServersInAWeightedTreeNetwork import Solution


@pytest.mark.parametrize(
    "edges, signalSpeed, output",
    [
        (
            [[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]],
            1,
            [0, 4, 6, 6, 4, 0],
        ),
        (
            [[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],
            3,
            [2, 0, 0, 0, 0, 0, 2],
        ),
    ],
)
class TestSolution:
    def test_countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.countPairsOfConnectableServers(
                edges,
                signalSpeed,
            )
            == output
        )
