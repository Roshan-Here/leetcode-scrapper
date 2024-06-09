import pytest
from q_2760_longestEvenOddSubarrayWithThreshold import Solution


@pytest.mark.parametrize(
    "nums, threshold, output",
    [([3, 2, 5, 4], 5, 3), ([1, 2], 2, 1), ([2, 3, 4, 5], 4, 3)],
)
class TestSolution:
    def test_longestAlternatingSubarray(
        self, nums: List[int], threshold: int, output: int
    ):
        sc = Solution()
        assert (
            sc.longestAlternatingSubarray(
                nums,
                threshold,
            )
            == output
        )
