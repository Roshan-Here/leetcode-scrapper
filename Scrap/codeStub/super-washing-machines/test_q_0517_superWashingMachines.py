import pytest
from q_0517_superWashingMachines import Solution


@pytest.mark.parametrize(
    "machines, output", [([1, 0, 5], 3), ([0, 3, 0], 2), ([0, 2, 0], -1)]
)
class TestSolution:
    def test_findMinMoves(self, machines: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMinMoves(
                machines,
            )
            == output
        )
