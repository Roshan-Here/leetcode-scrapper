import pytest
from q_0153_findMinimumInRotatedSortedArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([3, 4, 5, 1, 2], 1), ([4, 5, 6, 7, 0, 1, 2], 0), ([11, 13, 15, 17], 11)],
)
class TestSolution:
    def test_findMin(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMin(
                nums,
            )
            == output
        )
