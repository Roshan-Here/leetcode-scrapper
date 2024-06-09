import pytest
from q_0930_binarySubarraysWithSum import Solution


@pytest.mark.parametrize(
    "nums, goal, output", [([1, 0, 1, 0, 1], 2, 4), ([0, 0, 0, 0, 0], 0, 15)]
)
class TestSolution:
    def test_numSubarraysWithSum(self, nums: List[int], goal: int, output: int):
        sc = Solution()
        assert (
            sc.numSubarraysWithSum(
                nums,
                goal,
            )
            == output
        )
