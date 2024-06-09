import pytest
from q_2407_longestIncreasingSubsequenceIi import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([4, 2, 1, 4, 3, 4, 5, 8, 15], 3, 5),
        ([7, 4, 5, 1, 8, 12, 4, 7], 5, 4),
        ([1, 5], 1, 1),
    ],
)
class TestSolution:
    def test_lengthOfLIS(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.lengthOfLIS(
                nums,
                k,
            )
            == output
        )
