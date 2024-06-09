import pytest
from q_0034_findFirstAndLastPositionOfElementInSortedArray import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ],
)
class TestSolution:
    def test_searchRange(self, nums: List[int], target: int, output: List[int]):
        sc = Solution()
        assert (
            sc.searchRange(
                nums,
                target,
            )
            == output
        )
