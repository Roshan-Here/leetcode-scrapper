import pytest
from q_1493_longestSubarrayOf1SAfterDeletingOneElement import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 1, 0, 1], 3), ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5), ([1, 1, 1], 2)],
)
class TestSolution:
    def test_longestSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestSubarray(
                nums,
            )
            == output
        )
