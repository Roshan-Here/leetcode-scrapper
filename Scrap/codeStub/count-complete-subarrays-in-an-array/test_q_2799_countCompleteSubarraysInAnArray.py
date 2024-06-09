import pytest
from q_2799_countCompleteSubarraysInAnArray import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 1, 2, 2], 4), ([5, 5, 5, 5], 10)])
class TestSolution:
    def test_countCompleteSubarrays(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countCompleteSubarrays(
                nums,
            )
            == output
        )
