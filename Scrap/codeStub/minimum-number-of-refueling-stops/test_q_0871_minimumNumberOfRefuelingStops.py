import pytest
from q_0871_minimumNumberOfRefuelingStops import Solution


@pytest.mark.parametrize(
    "target, startFuel, stations, output",
    [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
    ],
)
class TestSolution:
    def test_minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.minRefuelStops(
                target,
                startFuel,
                stations,
            )
            == output
        )
