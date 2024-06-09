import pytest
from q_2871_splitArrayIntoMaximumNumberOfSubarrays import Solution


@pytest.mark.parametrize("nums, output", [([1, 0, 2, 0, 1, 2], 3), ([5, 7, 1, 3], 1)])
class TestSolution:
    def test_maxSubarrays(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSubarrays(
                nums,
            )
            == output
        )
