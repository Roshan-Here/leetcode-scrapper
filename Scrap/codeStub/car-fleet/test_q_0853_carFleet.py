import pytest
from q_0853_carFleet import Solution


@pytest.mark.parametrize(
    "target, position, speed, output",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
    ],
)
class TestSolution:
    def test_carFleet(
        self, target: int, position: List[int], speed: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.carFleet(
                target,
                position,
                speed,
            )
            == output
        )
