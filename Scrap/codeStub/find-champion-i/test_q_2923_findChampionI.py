import pytest
from q_2923_findChampionI import Solution


@pytest.mark.parametrize(
    "grid, output", [([[0, 1], [0, 0]], 0), ([[0, 0, 1], [1, 0, 1], [0, 0, 0]], 1)]
)
class TestSolution:
    def test_findChampion(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findChampion(
                grid,
            )
            == output
        )
