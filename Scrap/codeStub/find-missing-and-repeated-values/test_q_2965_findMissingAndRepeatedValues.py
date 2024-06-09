import pytest
from q_2965_findMissingAndRepeatedValues import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1, 3], [2, 2]], [2, 4]), ([[9, 1, 7], [8, 9, 2], [3, 4, 6]], [9, 5])],
)
class TestSolution:
    def test_findMissingAndRepeatedValues(
        self, grid: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findMissingAndRepeatedValues(
                grid,
            )
            == output
        )
