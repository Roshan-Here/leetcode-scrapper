import pytest
from q_2411_smallestSubarraysWithMaximumBitwiseOr import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 0, 2, 1, 3], [3, 3, 2, 2, 1]), ([1, 2], [2, 1])]
)
class TestSolution:
    def test_smallestSubarrays(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.smallestSubarrays(
                nums,
            )
            == output
        )
