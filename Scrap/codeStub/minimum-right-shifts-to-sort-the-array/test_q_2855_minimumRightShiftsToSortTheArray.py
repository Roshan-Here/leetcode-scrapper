import pytest
from q_2855_minimumRightShiftsToSortTheArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 4, 5, 1, 2], 2), ([1, 3, 5], 0), ([2, 1, 4], -1)]
)
class TestSolution:
    def test_minimumRightShifts(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumRightShifts(
                nums,
            )
            == output
        )
